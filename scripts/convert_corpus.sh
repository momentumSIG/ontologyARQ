#!/usr/bin/env bash
# Convert data/ PDFs to markdown under data_markdown/ mirroring the structure.
# Strategy per PDF:
#   1. markitdown (Microsoft, pure Python) -> markdown; if useful output (>= 1KB), done.
#   2. pypdf fallback -> plain text extracted per page; mark as pypdf.
#   3. both fail -> mark NEEDS_OCR in the manifest (no output file).
# Non-PDF files (.md/.owl/.ttl) are copied as-is. Specs PDFs are skipped.
#
# Usage: convert_corpus.sh [--fast] [--books] 
#   --fast  : only small files (analyses, articles, encyclopedia) - skip books dir
#   --books : include artículosJuan books (slow)

set -u
ROOT="/mnt/c/Users/48744372N/OneDrive - csic.es/Documentos/Tareas/ONTOLOGIA-ARQ"
DATA="$ROOT/data"
OUT="$ROOT/data_markdown"
VENV="/tmp/opencode/venv"
MANIFEST="$OUT/MANIFEST.csv"
MIN_CHARS=1000
FAST=0
BOOKS=0
for a in "$@"; do
  case "$a" in
    --fast) FAST=1 ;;
    --books) BOOKS=1 ;;
  esac
done

mkdir -p "$OUT"
[ -f "$MANIFEST" ] || echo "file,status,chars,method" > "$MANIFEST"

# Python fallback extractor
cat > /tmp/opencode/pypdf_extract.py <<'PYEOF'
import sys, os
from pypdf import PdfReader
path = sys.argv[1]
out = sys.argv[2]
try:
    r = PdfReader(path)
    parts = []
    for i, pg in enumerate(r.pages):
        try:
            t = pg.extract_text() or ""
        except Exception:
            t = ""
        parts.append(f"\n\n<!-- PAGE {i+1} -->\n\n{t}")
    text = "".join(parts)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(len(text))
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(1)
PYEOF

convert_one() {
  local src="$1" rel="$2"
  local outdir="$OUT/$(dirname "$rel")"
  local base; base="$(basename "$rel" .pdf)"
  local md="$outdir/$base.md"
  local tmp_any="$outdir/.$base.any.md"
  local tmp_py="$outdir/.$base.py.md"
  mkdir -p "$outdir"
  # idempotent: skip if already converted
  if [ -s "$md" ] && grep -q "^$rel," "$MANIFEST" 2>/dev/null; then
    echo "SKIP done   $rel"
    return 0
  fi

  # 1) markitdown (pure Python, no WSL/Windows path issues)
  local chars=0
  local out_md="$outdir/$base.md"
  timeout 120 "$VENV/bin/markitdown" "$src" -o "$out_md" >/dev/null 2>&1
  if [ -f "$out_md" ]; then
    chars=$(wc -c < "$out_md")
    # strip anydoc failure placeholder (watermark-only outputs are small anyway)
    if [ "$chars" -ge "$MIN_CHARS" ]; then
      echo "$rel,markitdown,$chars,markitdown" >> "$MANIFEST"
      echo "OK  markitdown  ${chars}B  $rel"
      return 0
    fi
  fi
  rm -f "$out_md" "$tmp_any"

  # 2) pypdf fallback
  local pyout=0
  pyout=$("$VENV/bin/python" /tmp/opencode/pypdf_extract.py "$src" "$tmp_py" 2>/dev/null) || pyout=0
  if [ "$pyout" -ge "$MIN_CHARS" ] 2>/dev/null; then
    mv "$tmp_py" "$md"
    echo "$rel,pypdf,$pyout,pypdf" >> "$MANIFEST"
    echo "OK  pypdf   ${pyout}B  $rel"
    return 0
  fi
  rm -f "$tmp_py"

  # 3) needs OCR
  echo "$rel,NEEDS_OCR,0,none" >> "$MANIFEST"
  echo "OCR $rel"
}

count=0
# Non-PDF files copied as-is
for f in $(find "$DATA" -type f ! -name "*.pdf" ! -name "*:Zone*" ! -name "~\$*"); do
  rel="${f#$DATA/}"
  mkdir -p "$OUT/$(dirname "$rel")"
  cp "$f" "$OUT/$rel" 2>/dev/null
done

LISTFILE="$(mktemp)"
find "$DATA" -type f -name "*.pdf" ! -name "*:Zone*" | sort > "$LISTFILE"
while IFS= read -r src; do
  rel="${src#$DATA/}"
  # skip specs PDFs
  case "$rel" in
    ontologies_data/pdfs/*) echo "SKIP specs $rel"; continue ;;
  esac
  # fast mode skips books
  if [ "$FAST" = "1" ]; then
    case "$rel" in
      artículosJuan/*) echo "SKIP book   $rel"; continue ;;
    esac
  fi
  # books mode is the default full run; --fast excludes them
  convert_one "$src" "$rel"
  count=$((count+1))
done < "$LISTFILE"
rm -f "$LISTFILE"

echo "=== done: $count PDFs processed ==="
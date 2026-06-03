import json
import math

# ============================================================
# PANEL 1: HEATMAP
# ============================================================

classes = [
    ("ArchaeologicalObject", 9, 9, 9),
    ("NaturalObject", 9, 9, 9),
    ("HumanMadeObject", 9, 9, 9),
    ("AbioticObject", 9, 9, 9),
    ("BioticObject", 9, 9, 9),
    ("Artefact", 9, 9, 9),
    ("Structure", 9, 9, 9),
    ("ArtisticExpression", 9, 9, 9),
    ("ManufacturingEvent", 9, 0, 0),
    ("UseEvent", 9, 0, 0),
    ("DepositionEvent", 9, 0, 0),
    ("RecoveryEvent", 9, 0, 0),
    ("ReuseEvent", 9, 0, 0),
    ("CirculationEvent", 9, 0, 0),
    ("TaphonomicAlterationEvent", 9, 0, 0),
    ("ObjectBiographyEvent", 7, 0, 0),
    ("IntactState", 0, 9, 0),
    ("FragmentedState", 0, 9, 0),
    ("DiscardedState", 0, 9, 0),
    ("ExcavatedState", 0, 9, 0),
    ("CuratedState", 0, 9, 0),
    ("RestoredState", 0, 7, 0),
    ("ExhibitedState", 0, 7, 0),
    ("MaterialAssignment", 0, 0, 9),
    ("FunctionalAssignment", 0, 0, 9),
    ("TypologicalAssignment", 0, 0, 9),
    ("ChronologicalAssignment", 0, 0, 9),
    ("InterpretiveClaim", 0, 0, 9),
    ("MeaningAssignment", 0, 0, 7),
    ("CustodyAssignment", 0, 0, 7),
    ("ProductionState", 0, 2, 0),
    ("ActiveUseState", 0, 2, 0),
    ("HeritageClaim", 0, 0, 2),
    ("DigitalReplica", 0, 0, 2),
    ("BiographicalPhase", 7, 0, 0),
    ("AnalyticalWorkflow", 7, 0, 0),
    ("PostDepositionalEvent", 9, 0, 0),
    ("ConservationState", 0, 5, 0),
    ("NarrativeBiography", 0, 0, 2),
    ("CertaintyAssessment", 0, 0, 2),
]

cols = ["D-P1", "D-P2", "D-P4", "K-P1", "K-P2", "K-P4", "Q-P1", "Q-P2", "Q-P4"]

cell_w = 52
cell_h = 22
header_h = 30
row_label_w = 180
margin = 20
title_h = 50
subtitle_h = 25
legend_h = 50

svg_w = margin * 2 + row_label_w + cell_w * len(cols)
svg_h = margin * 2 + title_h + subtitle_h + header_h + len(classes) * cell_h + legend_h

def color_for(val):
    if val == 0:
        return "#1a1a2e"
    elif val <= 2:
        return "#2d4a3e"
    elif val <= 5:
        return "#3a7d5e"
    elif val <= 7:
        return "#4caf70"
    else:
        return "#66ff99"

svg_parts = []
svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}">')
svg_parts.append(f'<rect width="{svg_w}" height="{svg_h}" fill="#0d1117"/>')

# Title
svg_parts.append(f'<text x="{margin}" y="{margin + 20}" fill="#ffffff" font-size="18" font-family="monospace" font-weight="bold">Panel 1: Mapa de Calor - Coincidencia de Clases</text>')
svg_parts.append(f'<text x="{margin}" y="{margin + 42}" fill="#8b949e" font-size="12" font-family="monospace">9 experimentos (3 modelos x 3 patrones) | 50 CQs unificadas propias | Temp 0.05</text>')

y = margin + title_h + subtitle_h

# Column headers
svg_parts.append(f'<text x="{margin + row_label_w + cell_w*0.5}" y="{y + 16}" fill="#8b949e" font-size="10" font-family="monospace" text-anchor="middle">D-P1</text>')
svg_parts.append(f'<text x="{margin + row_label_w + cell_w*1.5}" y="{y + 16}" fill="#8b949e" font-size="10" font-family="monospace" text-anchor="middle">D-P2</text>')
svg_parts.append(f'<text x="{margin + row_label_w + cell_w*2.5}" y="{y + 16}" fill="#8b949e" font-size="10" font-family="monospace" text-anchor="middle">D-P4</text>')
svg_parts.append(f'<text x="{margin + row_label_w + cell_w*3.5}" y="{y + 16}" fill="#8b949e" font-size="10" font-family="monospace" text-anchor="middle">K-P1</text>')
svg_parts.append(f'<text x="{margin + row_label_w + cell_w*4.5}" y="{y + 16}" fill="#8b949e" font-size="10" font-family="monospace" text-anchor="middle">K-P2</text>')
svg_parts.append(f'<text x="{margin + row_label_w + cell_w*5.5}" y="{y + 16}" fill="#8b949e" font-size="10" font-family="monospace" text-anchor="middle">K-P4</text>')
svg_parts.append(f'<text x="{margin + row_label_w + cell_w*6.5}" y="{y + 16}" fill="#8b949e" font-size="10" font-family="monospace" text-anchor="middle">Q-P1</text>')
svg_parts.append(f'<text x="{margin + row_label_w + cell_w*7.5}" y="{y + 16}" fill="#8b949e" font-size="10" font-family="monospace" text-anchor="middle">Q-P2</text>')
svg_parts.append(f'<text x="{margin + row_label_w + cell_w*8.5}" y="{y + 16}" fill="#8b949e" font-size="10" font-family="monospace" text-anchor="middle">Q-P4</text>')

y += header_h

# Rows
for i, (cls, p1, p2, p4) in enumerate(classes):
    vals = [p1, p2, p4, p1, p2, p4, p1, p2, p4]
    # Row label
    svg_parts.append(f'<text x="{margin + row_label_w - 5}" y="{y + 15}" fill="#c9d1d9" font-size="10" font-family="monospace" text-anchor="end">{cls}</text>')
    # Cells
    for j, v in enumerate(vals):
        x = margin + row_label_w + j * cell_w
        c = color_for(v)
        svg_parts.append(f'<rect x="{x}" y="{y}" width="{cell_w-1}" height="{cell_h-1}" fill="{c}" rx="2"/>')
        if v > 0:
            svg_parts.append(f'<text x="{x + cell_w*0.5}" y="{y + 15}" fill="#ffffff" font-size="10" font-family="monospace" text-anchor="middle">{v}</text>')
    y += cell_h

# Legend
y += 10
legend_x = margin + row_label_w
svg_parts.append(f'<text x="{legend_x}" y="{y + 12}" fill="#8b949e" font-size="10" font-family="monospace">Leyenda:</text>')
for val, label in [(9, "9/9 Universal"), (7, "7/9 Mayoría"), (2, "2/9 Minoría"), (0, "0 Ausente")]:
    svg_parts.append(f'<rect x="{legend_x + 70}" y="{y + 2}" width="14" height="14" fill="{color_for(val)}" rx="2"/>')
    svg_parts.append(f'<text x="{legend_x + 90}" y="{y + 13}" fill="#c9d1d9" font-size="10" font-family="monospace">{label}</text>')
    legend_x += 110

svg_parts.append('</svg>')

with open("docs/heatmap_classes.svg", "w") as f:
    f.write("\n".join(svg_parts))

print("heatmap_classes.svg created")

# ============================================================
# PANEL 3: RADAR CHART
# ============================================================

dimensions = ["Taxonomia", "Eventos", "Estados", "Asignaciones", "Disjoint", "Restricciones", "Reificacion", "CRMinf"]
qwen =    [9, 9, 8, 9, 8, 9, 9, 9]
deepseek =[8, 8, 7, 7, 6, 7, 7, 7]
kimi =    [7, 6, 5, 5, 4, 5, 5, 3]

n = len(dimensions)
angle_step = 2 * math.pi / n
cx, cy = 350, 320
max_r = 250

def polar_to_cart(angle, r):
    x = cx + r * math.cos(angle - math.pi/2)
    y = cy + r * math.sin(angle - math.pi/2)
    return x, y

svg_parts = []
svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="700" height="680" viewBox="0 0 700 680">')
svg_parts.append(f'<rect width="700" height="680" fill="#0d1117"/>')

# Title
svg_parts.append(f'<text x="350" y="30" fill="#ffffff" font-size="18" font-family="monospace" font-weight="bold" text-anchor="middle">Panel 3: Radar de Expresividad Ontologica</text>')
svg_parts.append(f'<text x="350" y="52" fill="#8b949e" font-size="12" font-family="monospace" text-anchor="middle">Comparacion de modelos en 8 dimensiones | Temp 0.05</text>')

# Grid circles
for level in [2, 4, 6, 8, 10]:
    r = max_r * level / 10
    pts = []
    for i in range(n):
        angle = i * angle_step
        x, y = polar_to_cart(angle, r)
        pts.append(f"{x:.1f},{y:.1f}")
    svg_parts.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="#30363d" stroke-width="1"/>')

# Axis lines
for i in range(n):
    angle = i * angle_step
    x, y = polar_to_cart(angle, max_r)
    svg_parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#30363d" stroke-width="1"/>')

# Dimension labels
for i, dim in enumerate(dimensions):
    angle = i * angle_step
    x, y = polar_to_cart(angle, max_r + 30)
    svg_parts.append(f'<text x="{x:.1f}" y="{y:.1f}" fill="#8b949e" font-size="12" font-family="monospace" text-anchor="middle">{dim}</text>')

# Data polygons
def make_polygon(data, color, fill_opacity):
    pts = []
    for i, v in enumerate(data):
        angle = i * angle_step
        r = max_r * v / 10
        x, y = polar_to_cart(angle, r)
        pts.append(f"{x:.1f},{y:.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{color}" fill-opacity="{fill_opacity}" stroke="{color}" stroke-width="2"/>'

svg_parts.append(make_polygon(kimi, "#f85149", 0.15))
svg_parts.append(make_polygon(deepseek, "#58a6ff", 0.15))
svg_parts.append(make_polygon(qwen, "#3fb950", 0.15))

# Data points
def make_points(data, color):
    result = ""
    for i, v in enumerate(data):
        angle = i * angle_step
        r = max_r * v / 10
        x, y = polar_to_cart(angle, r)
        result += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}"/>'
    return result

svg_parts.append(make_points(kimi, "#f85149"))
svg_parts.append(make_points(deepseek, "#58a6ff"))
svg_parts.append(make_points(qwen, "#3fb950"))

# Legend
legend_y = 620
svg_parts.append(f'<circle cx="120" cy="{legend_y}" r="6" fill="#3fb950"/>')
svg_parts.append(f'<text x="135" y="{legend_y + 4}" fill="#3fb950" font-size="12" font-family="monospace">Qwen3.6 (maxima expresividad)</text>')
svg_parts.append(f'<circle cx="350" cy="{legend_y}" r="6" fill="#58a6ff"/>')
svg_parts.append(f'<text x="365" y="{legend_y + 4}" fill="#58a6ff" font-size="12" font-family="monospace">Deepseek-v4-pro (equilibrado)</text>')
svg_parts.append(f'<circle cx="560" cy="{legend_y}" r="6" fill="#f85149"/>')
svg_parts.append(f'<text x="575" y="{legend_y + 4}" fill="#f85149" font-size="12" font-family="monospace">Kimi-2.6 (conciso)</text>')

svg_parts.append('</svg>')

with open("docs/radar_expressiveness.svg", "w") as f:
    f.write("\n".join(svg_parts))

print("radar_expressiveness.svg created")

# ============================================================
# PANEL 2: PATTERN COMPARISON DIAGRAM
# ============================================================

svg_parts = []
svg_w = 1100
svg_h = 750
svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}">')
svg_parts.append(f'<rect width="{svg_w}" height="{svg_h}" fill="#0d1117"/>')

# Title
svg_parts.append(f'<text x="550" y="30" fill="#ffffff" font-size="18" font-family="monospace" font-weight="bold" text-anchor="middle">Panel 2: Comparacion de Patrones - Modelado del mismo fenomeno</text>')
svg_parts.append(f'<text x="550" y="52" fill="#8b949e" font-size="12" font-family="monospace" text-anchor="middle">Anfora Dressel 20: produccion - uso - deposicion - recuperacion | Temp 0.05</text>')

# Column headers
col_w = 320
col_x = [50, 390, 730]
colors = ["#58a6ff", "#3fb950", "#f85149"]
titles = ["P1: Event-Driven", "P2: State-Transition", "P4: Assignment-Intrinsic"]
subtitles = ["Cadena de eventos", "Secuencia de estados", "Cadena de asignaciones"]

for i in range(3):
    x = col_x[i]
    svg_parts.append(f'<rect x="{x}" y="70" width="{col_w}" height="30" fill="{colors[i]}" fill-opacity="0.2" rx="4"/>')
    svg_parts.append(f'<text x="{x + col_w/2}" y="90" fill="{colors[i]}" font-size="14" font-family="monospace" font-weight="bold" text-anchor="middle">{titles[i]}</text>')
    svg_parts.append(f'<text x="{x + col_w/2}" y="110" fill="#8b949e" font-size="11" font-family="monospace" text-anchor="middle">{subtitles[i]}</text>')

# P1: Event-Driven boxes
p1_events = [
    ("ProductionEvent", 130),
    ("UseEvent", 210),
    ("DepositionEvent", 290),
    ("RecoveryEvent", 370),
]
for label, y in p1_events:
    svg_parts.append(f'<rect x="{col_x[0]+30}" y="{y}" width="{col_w-60}" height="50" fill="#161b22" stroke="#58a6ff" stroke-width="1.5" rx="6"/>')
    svg_parts.append(f'<text x="{col_x[0]+col_w/2}" y="{y+28}" fill="#c9d1d9" font-size="12" font-family="monospace" text-anchor="middle">{label}</text>')

# Arrows P1
for i in range(len(p1_events)-1):
    y1 = p1_events[i][1] + 50
    y2 = p1_events[i+1][1]
    svg_parts.append(f'<line x1="{col_x[0]+col_w/2}" y1="{y1}" x2="{col_x[0]+col_w/2}" y2="{y2}" stroke="#58a6ff" stroke-width="2" marker-end="url(#arrow)"/>')

# P2: State-Transition boxes
p2_states = [
    ("IntactState", 130),
    ("FragmentedState", 210),
    ("DiscardedState", 290),
    ("ExcavatedState", 370),
]
for label, y in p2_states:
    svg_parts.append(f'<rect x="{col_x[1]+30}" y="{y}" width="{col_w-60}" height="50" fill="#161b22" stroke="#3fb950" stroke-width="1.5" rx="6"/>')
    svg_parts.append(f'<text x="{col_x[1]+col_w/2}" y="{y+28}" fill="#c9d1d9" font-size="12" font-family="monospace" text-anchor="middle">{label}</text>')

# Arrows P2
for i in range(len(p2_states)-1):
    y1 = p2_states[i][1] + 50
    y2 = p2_states[i+1][1]
    svg_parts.append(f'<line x1="{col_x[1]+col_w/2}" y1="{y1}" x2="{col_x[1]+col_w/2}" y2="{y2}" stroke="#3fb950" stroke-width="2"/>')

# P4: Assignment-Intrinsic boxes
p4_assigns = [
    ("MaterialAssignment", 130),
    ("FunctionalAssignment", 210),
    ("TypologicalAssignment", 290),
    ("ChronologicalAssignment", 370),
]
for label, y in p4_assigns:
    svg_parts.append(f'<rect x="{col_x[2]+30}" y="{y}" width="{col_w-60}" height="50" fill="#161b22" stroke="#f85149" stroke-width="1.5" rx="6"/>')
    svg_parts.append(f'<text x="{col_x[2]+col_w/2}" y="{y+28}" fill="#c9d1d9" font-size="11" font-family="monospace" text-anchor="middle">{label}</text>')

# Arrows P4
for i in range(len(p4_assigns)-1):
    y1 = p4_assigns[i][1] + 50
    y2 = p4_assigns[i+1][1]
    svg_parts.append(f'<line x1="{col_x[2]+col_w/2}" y1="{y1}" x2="{col_x[2]+col_w/2}" y2="{y2}" stroke="#f85149" stroke-width="2"/>')

# Object box at top
svg_parts.append(f'<rect x="400" y="130" width="300" height="50" fill="#161b22" stroke="#ffffff" stroke-width="2" rx="6"/>')
svg_parts.append(f'<text x="550" y="158" fill="#ffffff" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">ArchaeologicalObject: Dressel 20</text>')

# Lines from object to first element of each pattern
svg_parts.append(f'<line x1="400" y1="155" x2="370" y2="155" stroke="#8b949e" stroke-width="1" stroke-dasharray="4"/>')
svg_parts.append(f'<line x1="700" y1="155" x2="730" y2="155" stroke="#8b949e" stroke-width="1" stroke-dasharray="4"/>')

# Notes at bottom
notes_y = 460
svg_parts.append(f'<text x="50" y="{notes_y}" fill="#58a6ff" font-size="12" font-family="monospace" font-weight="bold">P1: Enfoque en eventos</text>')
svg_parts.append(f'<text x="50" y="{notes_y+20}" fill="#8b949e" font-size="11" font-family="monospace">Modela el WHAT HAPPENED')
svg_parts.append(f'<text x="50" y="{notes_y+38}" fill="#8b949e" font-size="11" font-family="monospace">Cada evento es una instancia de crm:E5_Event')
svg_parts.append(f'<text x="50" y="{notes_y+56}" fill="#8b949e" font-size="11" font-family="monospace">El objeto es participante (crm:P102_fell_within)')

svg_parts.append(f'<text x="390" y="{notes_y}" fill="#3fb950" font-size="12" font-family="monospace" font-weight="bold">P2: Enfoque en estados</text>')
svg_parts.append(f'<text x="390" y="{notes_y+20}" fill="#8b949e" font-size="11" font-family="monospace">Modela el HOW IT IS')
svg_parts.append(f'<text x="390" y="{notes_y+38}" fill="#8b949e" font-size="11" font-family="monospace">Cada estado es una condicion del objeto')
svg_parts.append(f'<text x="390" y="{notes_y+56}" fill="#8b949e" font-size="11" font-family="monospace">Transiciones implicitas entre estados')

svg_parts.append(f'<text x="730" y="{notes_y}" fill="#f85149" font-size="12" font-family="monospace" font-weight="bold">P4: Enfoque en asignaciones</text>')
svg_parts.append(f'<text x="730" y="{notes_y+20}" fill="#8b949e" font-size="11" font-family="monospace">Modela el WHAT WE KNOW')
svg_parts.append(f'<text x="730" y="{notes_y+38}" fill="#8b949e" font-size="11" font-family="monospace">Cada asignacion es un acto interpretativo')
svg_parts.append(f'<text x="730" y="{notes_y+56}" fill="#8b949e" font-size="11" font-family="monospace">Separa objeto de interpretacion')

# Key insight box
svg_parts.append(f'<rect x="50" y="{notes_y+100}" width="1000" height="80" fill="#161b22" stroke="#8b949e" stroke-width="1" rx="6"/>')
svg_parts.append(f'<text x="550" y="{notes_y+125}" fill="#ffffff" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">Conclusion clave:</text>')
svg_parts.append(f'<text x="550" y="{notes_y+148}" fill="#8b949e" font-size="12" font-family="monospace" text-anchor="middle">Los 3 patrones modelan el mismo fenomeno arqueologico pero desde perspectivas complementarias:')
svg_parts.append(f'<text x="550" y="{notes_y+168}" fill="#8b949e" font-size="12" font-family="monospace" text-anchor="middle">P1 = realidad historica (eventos) | P2 = condicion material (estados) | P4 = conocimiento arqueologico (asignaciones)')

svg_parts.append('</svg>')

with open("docs/pattern_comparison.svg", "w") as f:
    f.write("\n".join(svg_parts))

print("pattern_comparison.svg created")

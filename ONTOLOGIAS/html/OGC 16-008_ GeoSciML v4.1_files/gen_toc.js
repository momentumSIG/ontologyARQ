$( document ).ready(function() {


var encodeHtmlEntity = function(str) {
  var buf = [];
  for (var i=str.length-1;i>=0;i--) {
    buf.unshift(['&#', str[i].charCodeAt(), ';'].join(''));
  }
  return buf.join('');
};


	// Auto number the annexes (must have class="autoannex" )
	// Must do this first so that the Annexes will be listed with their auto numbering
	var myArray = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ];
	$(".autoannex").each( function() {
		var val = myArray[ 0 ];
		$(this).prepend(val);
	// set id of parent <h1> to the auto number 	
		$(this).parent("h1").attr( "id", val );
		myArray.shift(); 
	});
	
	// Auto number the Figures (must have class="autofigure" )
	// Must do this first so that the figures will be listed with their auto numbering
	var figure_ctr = 0;
	$(".autofigure").each( function() {
		figure_ctr++;
		var val = figure_ctr;
		$(this).prepend(val);
		var figure_val = "figure_" + val;
	// set id of parent <figure> to the auto number 	
	$(this).parent().parent().attr( {"id": figure_val });
	});
	
	// Auto number the Tables (must have class="autotable" )
	// Must do this first so that the figures will be listed with their auto numbering
	var table_ctr = 0;
	$(".autotable").each( function() {
		table_ctr++;
		var val = table_ctr;
		var table_val = "table_" + val;
		$(this).prepend(val);
//		$(this).prepend("<a name='"+table_val+"'></a>");
	// set id of parent <caption> to the auto number 	
	$(this).parent().parent().attr( {"id": table_val });
	});	
	
	// Auto number the Tables (must have class="autotable" )
	// Must do this first so that the figures will be listed with their auto numbering
	var requirement_ctr = 0;
	$(".requirement").each( function() {
		requirement_ctr++;
		var val = requirement_ctr;
		var requirement_val = "requirement_" + val;
	// set id of parent <requirement> to the auto number 	
	$(this).attr( {"id": requirement_val });
	});	
	
	
	
	// Now run the TOC Generator. TOT and TOF Generator
	var newLine, el, title, link, last;
	var toc_counter = 0;	
	var counter = 0;	

	var tof_counter = 0;
	var tot_counter = 0;
	var tor_counter = 0;
	var ToC =
	  "<nav role='navigation' id='toc' class='table-of-contents'>"
		+ "<header>"
		+ "<p class='prefacehead'>Table of Contents</p>"
		+ "</header>"
		+ "<ul>";
	$("section :header").each(function() {
		if ($(this).is("h1")) {
			while( last > 1 ){
				ToC += "</ul>";
				last = last - 1;
			}
			last = "1";
		} else if ($(this).is("h2")) {
			if (last < 2) { 
				ToC += "<ul>";
			}	
			while( last > 2 ){
				ToC += "</ul>";
				last = last - 1;
			}
			last = "2";
		} else if ($(this).is("h3")) {
			if (last < 3) {
				ToC += "<ul>";
			}
			while( last > 3 ){
				ToC += "</ul>";
				last = last - 1;
			}
			last = "3";
		} else if ($(this).is("h4")) {
			if (last < 4) {
				ToC += "<ul>";
			}
			while( last > 4 ){
				ToC += "</ul>";
				last = last - 1;
			}
			last = "4";
		} else if ($(this).is("h5")) {
			if (last < 5) { ToC += "<ul>"; }
			while( last > 5 ){ ToC += "</ul>"; last = last - 1; }
			last = "5";
		} else if ($(this).is("h6")) {
			if (last < 6) { ToC += "<ul>"; }
			last = "6";
		}
                counter++;
		el = $(this);
		title = el.text();
		if (el.attr("id")) {
			link = "#" + counter; 
		} else {
			toc_counter++;
			link = "#" + counter; 
		}
		$(this).prepend("<a name='"+counter+"'></a>");
		newLine =
			"<li>" +
			"<a href='" + link + "'>" +
			title +
			"</a>" +
			"</li>";
		ToC += newLine;
	}); 
	ToC +=
		"</ul>" +
		"</nav>";
	if (figure_ctr) {
		ToC +=
			"<nav role='navigation' id='tof' class='table-of-contents'>"
				+ "<header>"
				+ "<p class='prefacehead'>Table of Figures</p>"
				+ "</header>"
				+ "<dir><ul>";

		$("figure").each(function() {
			if ($(this).children("figcaption")[0]) {
				el = $(this);	
				title = el.text();
				if (el.attr("id")) {
					link = "#" + el.attr("id");				
				} else {
					tof_counter++;
					link = "#" + tof_counter;
				}
				newLine =
					"<li>" +
					"<a href='" + link + "'>" +
					title +
					"</a>" +
					"</li>";
				ToC += newLine;
			}
		});
		ToC +=
			"</ul></dir>" +
			"</nav>";
	}
	if (table_ctr) {
		ToC +=
			"<nav role='navigation' id='tot' class='table-of-contents'>"
			+ "<header>"
			+ "<p class='prefacehead'>Table of Tables</p>"
			+ "</header>"
			+ "<dir><ul>";
//		$("table").each(function() {
		$(".tableauto").each(function() {
			if ($(this).children("caption")) {
				el = $(this).children("caption");
				title = el.text();
				if (el.attr("id")) {
					link = "#table_" + el.attr("id");				
				} else {
					tot_counter++;
					link = "#table_" + tot_counter;
				}
                                if (title) {
                                  title = encodeHtmlEntity(title); 
				  newLine =
				  "<li>" +
				  "<a href='" + link + "'>" +
				  title +
				  "</a>" +
		  		  "</li>";
				  ToC += newLine;
                                }
			}
		});
		ToC +=
		"</ul></dir>" +
		"</nav>";
	}
	if (requirement_ctr) {
		ToC +=
			"<nav role='navigation' id='tor' class='table-of-contents'>"
			+ "<header>"
			+ "<p class='prefacehead'>Table of Requirements</p>"
			+ "</header>"
			+ "<dir><ul>";
		$(".requirement").each(function() {
			if ($(this).children("td.requirementlabel").eq(0) || $(this).children("th.requirementlabel").eq(0)) {
				el = $(this).find('td.requirementlabel').eq(0);
				el = $(this).find('th.requirementlabel').eq(0);
				title = el.text();
				if (el.attr("id")) {
					link = "#" + el.attr("id");				
				} else {
					tor_counter++;
					link = "#requirement_" + tor_counter;
				}
				newLine =
				"<li>" +
				"<a href='" + link + "'>" +
				title +
				"</a>" +
				"</li>";
				ToC += newLine;
			}
		});
	}
	ToC +=
		"</ul></dir>" +
		"</nav>";
	$(".all-headings").prepend(ToC);
});

google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(function() {
	$(function() {
		$.getJSON("/ajax/" + $("#ajax").html() + "/", function(data) {
			$("#chart").empty();
			if (data.length == 0) {
				$("#chart").html("<p>You haven't practiced yet. Go <a href=\"/practice/\">practice</a>!</p>");
				return;
			}
			var data = google.visualization.arrayToDataTable(data);

			var options = {
				title: 'Performance',
				vAxes: {
					0: {logScale: false, minValue: 0, maxValue: 100},
					1: {logScale: false, minValue: 0}
				},
				series: {
					0: {targetAxisIndex: 0},
					1: {targetAxisIndex: 1}
				},
			};

			var chart = new google.visualization.LineChart(document.getElementById('chart'));
			chart.draw(data, options);
		});
	});
});

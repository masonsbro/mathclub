$(function() {
	window.setInterval(function() {
		$("#time").val(parseInt($("#time").val()) + 1);
	}, 1000);
});
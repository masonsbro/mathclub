$(function() {
	window.setInterval(function() {
		$("#time").val(parseInt($("#time").val()) + 1);
	}, 1000);

	$('#answer').each(function() {
		var elem = $(this);
		// Save current value of element
		elem.data('oldVal', elem.val());
		// Look for changes in the value
		elem.bind("propertychange keyup input paste", function(event) {
			// If value has changed...
			if (elem.data('oldVal') != elem.val()) {
				if (elem.val().substring(1, elem.val().length) != elem.data('oldVal') &&
					elem.val().substring(0, elem.val().length - 1) != elem.data('oldVal')) {
					elem.val(elem.data('oldVal'));
				} else {
					elem.data('oldVal', elem.val());
				}
			}
		});
	});
});
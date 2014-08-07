$(function() {
	$("#skill").change(function(event) {
		$("#learn_item optgroup").remove();
		$("#learn_item option:gt(0)").remove();
		$("#learn_item").append("<option value=\"-1\">Loading tricks...</option>")
		$.getJSON("/ajax/learn_items/skill/" + $("#skill").val() + "/", function(data) {
			$("#learn_item option:gt(0)").remove();
			data.forEach(function(element) {
				$("#learn_item").append("<option value=\"" + element.pk + "\">" + element.fields.title + "</option>");
			});
		});
	});
	// update as soon as page loads if already selected (i.e. editing)
	if ($("#skill").val() != "-1") {
		$("#skill").change();
	}
});

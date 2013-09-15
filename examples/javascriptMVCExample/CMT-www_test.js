steal(
	'funcunit',
	function (S) {

	// this tests the assembly 
	module("CMT-www", {
		setup : function () {
			S.open("//github.com/osblinnikov/SNocs/examples/javascriptMVCExample/index.html");
		}
	});

	test("welcome test", function () {
		equals(S("h1").text(), "Welcome to JavaScriptMVC!", "welcome text");
	});

});

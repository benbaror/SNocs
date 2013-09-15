//js ../../../airu.com/CMT-www/scripts/doc.js

load('steal/rhino/rhino.js');
steal("documentjs", function(DocumentJS){
	DocumentJS('../../../airu.com/CMT-www/index.html', {
		out: 'CMT-www/docs',
		markdown : ['CMT-www', 'steal', 'jquerypp', 'can', 'funcunit'],
		parent : 'CMT-www'
	});
});
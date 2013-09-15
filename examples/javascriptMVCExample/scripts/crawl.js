// load('../../../airu.com/CMT-www/scripts/crawl.js')

load('steal/rhino/rhino.js')

steal('steal/html/crawl', function(){
  steal.html.crawl("../../../airu.com/CMT-www/CMT-www.html","../../../airu.com/CMT-www/out")
});

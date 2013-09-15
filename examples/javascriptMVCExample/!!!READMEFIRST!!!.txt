 This Project is aimed to show you how to create javascriptMVC builds with SNocs wrapper. 
 First of all you need install javascriptMVC in your Projects/src/ directory.
 If you follow golang workspace structure convention JavascriptMVC would be placed at:
 
 Projects/src/github.com/bitovi/javascriptmvc/
 
 After dowloading javascriptMVC you need to fix the paths to the steal, jquerypp, jmvc ...
for this puprose add the following lines at the begining of 

Projects/src/github.com/bitovi/javascriptmvc/stealconfig.js 

stealRootPath = '../../../'
jmvcRootPath = 'github.com/bitovi/javascriptmvc/'

also, add the root section to the steal.config :

},
root: steal.config('root').join(stealRootPath),
paths: {

fix the paths to the libraries like in the following code:

paths: {
    // "jquery/": "jquerypp/",
    // "jquery": "can/lib/jquery.1.9.1.js",
    // "mootools/mootools.js" : "can/lib/mootools-core-1.4.5.js",
    // "dojo/dojo.js" : "can/util/dojo/dojo-1.8.1.js",
    // "yui/yui.js" : "can/lib/yui-3.7.3.js",
    // "zepto/zepto.js" : "can/lib/zepto.1.0rc1.js"
    "can/": jmvcRootPath+"can/",
    "steal/" : jmvcRootPath+"steal/",
    "jquery/": jmvcRootPath+"jquerypp/",
    "jquery": jmvcRootPath+"can/lib/jquery.1.9.1.js",
    "mootools/mootools.js" : jmvcRootPath+"can/lib/mootools-core-1.4.5.js",
    "dojo/dojo.js" : jmvcRootPath+"can/util/dojo/dojo-1.8.1.js",
    "yui/yui.js" : jmvcRootPath+"can/lib/yui-3.7.3.js",
    "zepto/zepto.js" : jmvcRootPath+"can/lib/zepto.1.0rc1.js"
},

this is all you have to do with stealconfig.js

I can give you small tips how to create the projects and controllers in the unusual for javascriptMVC 
workspace, in Linux:

./js jmvc/generate/app ../../../icanchangethisdomain/ProjectName

in Windows:
.\js jmvc\generate\app ..\..\..\icanchangethisdomain.com\ProjectName

this is not the end. For some reason Javascript MVC 3.3 can't generate good paths to the projects
which is created not in the javascriptmvc root folder.

You have to manually fix them in index.html, test.html and *.js files of your generated project.
Fix the steal path in index.html:

../../github.com/bitovi/javascriptmvc/steal/steal.js?icanchangethisdomain/ProjectName/ProjectName.js

in test.html:

../../github.com/bitovi/javascriptmvc/steal/steal.js?icanchangethisdomain/ProjectName/ProjectName_test.js

in ProjectName_test.js:

//icanchangethisdomain/ProjectName/index.html

Now you can generate production.js , .css with SNocs by simply adding SConscript from the current folder to 
the 

icanchangethisdomain/ProjectName/ 

to build production simply type following command in command line:

snocs icanchangethisdomain/ProjectName -r

-r flag means that SNocs should not use any compilers information from SCons for running SConscript
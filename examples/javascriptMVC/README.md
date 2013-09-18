 This Project is aimed to show you how to create javascriptMVC builds with SNocs wrapper. 
 First of all you need install javascriptMVC in current folder so:
jmvc, steal, jquerypp and other folders should be placed right here in this folder.

after that generate or copy your application in the currentfolder/main/

this is convention, you can fix the path in the SConscript file.

After getting javascriptMVC and your application installed you can simply run snocs in the current folder. To make the preparation of SNocs faster add -r option to the snocs, so the snocs whould not initialize the SCons building system, but simply Run SConscript as a python file.

Results of the build will be placed in the main_production folder
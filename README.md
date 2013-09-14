SNocs
=====

SNocs is a wrapper for SCons Software Construction tool (www.scons.org)

If you find SCons low level system then SNocs will help you to boost your efficiency in C/C++ development workflows

SNocs simplifies SCons project configuration:

1. SNocs is able to build any project from your's workspace even you are not in project directory.
2. You can set dependencies in SConscript that SNocs will automatically build them.
3. SNocs allows you to choose compiler, platform and configuration in command line.
4. SNocs enables you to set up Unit tests for the project.
5. SNocs is integrated into golang workspace structure. (http://golang.org/doc/code.html)
6. It can be used with another projects workspace structure

Usage:

snocs [SconscriptFilePath] [options]

SconscriptFilePath can be absolute or relative to current path or 
relative to workspace sources root directory e.g.:

    snocs github.com\osblinnikov\SNocs\examples\helloWorld compiler=vc9 test

Available SNocs options:

    compiler={g++,mingw,vc9,vc10,vc11,vc11exp}
    configuration={Debug,Release}
    platform={x86,Win32,x64} # Win32 is an alias to x86
    verbose=1 # enables scons debug output

Other options could be specific for SCons. 

Examples:

    snocs .. compiler=vc9 platform=x86 configuration=Debug
    snocs test -Q           #builds and runs tests with reduced log
    snocs install -c        #cleans installation

If you want to change default path to the Projects workspace directory just change 'PROJECTS_ROOT_PATH' variable in 'builder.py' file. 

During test phase of building, SNocs extends it's LD_LIBRARY_PATH to provide searching for shared libraries

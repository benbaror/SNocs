snocs
=====

Snocs is a little wrapper on SCons Software Construction tool (www.scons.org)

If you found SCons too low level then Snocs will help you to rise the level of abstraction for the C/C++ builds

1. Snocs builds any project from your Projects directory even if your current directory somewhere else now.
2. You can set dependencies in project's SConscript and snocs will automatically call dependent SConscripts.
3. Snocs helps you with choosing compiler, platform and configuration for your build.
4. Enables you to setup Unit tests for your project.
5. Integrated into golang Projects workspace structure. (http://golang.org/doc/code.html)
6. Can be used with another Projects workspace structure, simply edit the builder.py.

Usage:

snocs [SconscriptFilePath] [options]

Examples:

    snocs .. compiler=vc9 platform=x86 configuration=Debug
    snocs test -Q           #build and run tests with reduced log
    snocs install -c        #clean installation
    
SconscriptFilePath can be absolute, relative to current path, or 
relative to projects root path e.g.:
    
    snocs github.com\osblinnikov\snocs\examples\helloWorld compiler=vc9 test

Available options:

    compiler={g++,mingw,vc9,vc10,vc11,vc11exp}
    configuration={Debug,Release}
    platform={x86,Win32,x64} # Win32 is an alias to x86
    verbose=1 # enables scons debug output

Other options could be SCons specific. If you want to change default path to the Projects directory please see the builder.py file and PROJECTS_ROOT_PATH variable. During 'test' phase snocs updates LD_LIBRARY_PATH local copy to provide of shared libraries

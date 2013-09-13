#! /usr/bin/env python
import os.path
import sys
import os
from builder import PROJECTS_ROOT_PATH
from builder import printHelp
Sconscript = None
firstRealArgI = 1
#in case we don't have any arguments
if len(sys.argv) <= firstRealArgI:
    #try to find the sconscript right here
    if os.path.exists(os.path.join(os.getcwd(),"Sconscript")):
        firstRealArgI = firstRealArgI - 1
        Sconscript = os.path.join(os.getcwd(),"Sconscript")
    else:
        print "No Sconscript files found"
        printHelp()
        exit()
else:
    #try to find the sconscript right here
    if os.path.exists(os.path.join(os.getcwd(),"Sconscript")):
        firstRealArgI = firstRealArgI - 1
        Sconscript = os.path.join(os.getcwd(),"Sconscript")
    #try to find the sconscript in the specified absolute path
    elif os.path.exists(os.path.join(sys.argv[firstRealArgI],"Sconscript")):
        Sconscript = os.path.join(sys.argv[firstRealArgI],"Sconscript")
    #try to find the sconscript in the specified relative to current path
    elif os.path.exists(os.path.join(os.getcwd(),sys.argv[firstRealArgI],"Sconscript")):
        Sconscript = os.path.join(os.getcwd(),sys.argv[firstRealArgI],"Sconscript")
    #try to find the sconscript in the specified path from projects src root
    elif os.path.exists(os.path.join(PROJECTS_ROOT_PATH,'src',sys.argv[firstRealArgI],"Sconscript")):
        Sconscript = os.path.join(PROJECTS_ROOT_PATH,'src',sys.argv[firstRealArgI],"Sconscript")
    else:
        print "No "+os.path.join(os.getcwd(),"Sconscript")
        print "No "+os.path.join(sys.argv[firstRealArgI],"Sconscript")
        print "No "+os.path.join(os.getcwd(),sys.argv[firstRealArgI],"Sconscript")
        print "No "+os.path.join(PROJECTS_ROOT_PATH,'src',sys.argv[firstRealArgI],"Sconscript")
        print "NO Sconscript files found"
        printHelp()
        exit()
    
OTHER_ARGUMENTS = ""
if len(sys.argv) > firstRealArgI + 1:
    for i in range(firstRealArgI+1, len(sys.argv)):
        if sys.argv[i] == '-h':
            printHelp()
            exit()
        OTHER_ARGUMENTS+=" "+sys.argv[i]
        
os.system("scons -f "+os.path.abspath(os.path.dirname(__file__))+"/Sconstruct sconscript="+Sconscript+OTHER_ARGUMENTS)
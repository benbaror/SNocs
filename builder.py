import os.path
import sys
from gpp import *
from mingw import *
from default import *
from vc9 import *

#PLEASE change it if you don't want the standard snocs location
PROJECTS_ROOT_PATH = os.path.abspath(os.path.dirname(__file__)+'/../../../../')

def prepare_args(ARGUMENTS):
    #--------command line arguments------------
    args = {}
    args['SCONSCRIPT'] = ARGUMENTS.get('sconscript', None)
    if args['SCONSCRIPT'] == None or args['SCONSCRIPT']=="":
        print "Sconscript is not specified!"
        exit()
    args['configuration'] = ARGUMENTS.get('configuration', 'Release')
    if args['configuration'] == 'debug':
        args['configuration'] = 'Debug'
    if args['configuration'] != 'Debug':
        args['configuration'] = 'Release'
    args['COMPILER_CODE'] = ARGUMENTS.get('compiler', 'default').lower()
    args['TARGET_ARCH'] = ARGUMENTS.get('platform', 'x86').lower()
    if args['TARGET_ARCH'] == 'Win32':
        args['TARGET_ARCH'] = 'x86'
    args['TARGET_ARCH'] = args['TARGET_ARCH'].lower()
    args['CCCOMSTR'] = None
    args['LINKCOMSTR'] = None
    if ARGUMENTS.get('verbose') != "1":
        args['CCCOMSTR'] = "Compiling $TARGET"
        args['LINKCOMSTR'] = "Linking $TARGET"
    #--------deploy parameters--------
    args['PROJECTS_ROOT_PATH'] = PROJECTS_ROOT_PATH
    args['INSTALL_PATH'] = os.path.join(args['PROJECTS_ROOT_PATH'],'bin')
    args['INSTALL_ALIASES'] = [] #here will be the targets for install alias
    args['TEST_ALIASES'] = [] #here will be the targets for test alias
    args['ARCHITECTURE_CODE'] = '_'+args['COMPILER_CODE']+'_'+args['TARGET_ARCH']
    #---------init params-----------
    args['PassedTestsOutputFileName'] = "tests_"+args['configuration']+args['ARCHITECTURE_CODE']+".passed"
    args['MSVC_PDB'] = 0
    args['MSVC_VERSION'] = None
    args['APP_DEPENDENCIES'] = {}
    args['APP_BUILD'] = {}
    args['TOOLS'] = 'default'
    args['LINKFLAGS'] = []
    args['CCFLAGS'] = []
    args['LIBS'] = []
    args['LIBPATH']=[args['INSTALL_PATH']]
    args['PROJECTS_SRC_PATH'] = os.path.join(args['PROJECTS_ROOT_PATH'],'src')
    args['CPPPATH'] = [
        args['PROJECTS_SRC_PATH']
    ]
    args['CPPDEFINES'] = []
    #--------SWITCHING COMPILER------
    if args['COMPILER_CODE'] == 'default':
        print "WARNING: compiler was not specified, using default parameters"
        args = prepare_default(args)
    elif args['COMPILER_CODE'] == 'g++':
        args = prepare_gpp(args)
    elif args['COMPILER_CODE'] == 'mingw':
        args = prepare_mingw(args)
    elif args['COMPILER_CODE'] == 'vc9':
        args = prepare_vc9(args)
    elif args['COMPILER_CODE'] == 'vc10':
        args = prepare_vc9(args)
        args['MSVC_VERSION'] = '10.0'
    elif args['COMPILER_CODE'] == 'vc11':
        args = prepare_vc9(args)
        args['MSVC_VERSION'] = '11.0'
    elif args['COMPILER_CODE'] == 'vc11exp':
        args = prepare_vc9(args)
        args['MSVC_VERSION'] = '11.0Exp'
    else:
        print "Unknown compiler: "+args['COMPILER_CODE']
        exit()
    return args

def builder_unit_test(target, source, env):
    app = str(source[0].abspath)
    if os.spawnl(os.P_WAIT, app, app)==0:
        open(str(target[0]),'w').write("PASSED: "+source[0].path+"\n")
    else:
        open(str(target[0]),'w').write("FAILED: "+source[0].path+"\n")
        return 1

def printHelp():
    print "**********************"
    print "Snocs is a little wrapper on SCons Software Construction tool (http://www.scons.org/)."
    print "Usage: snocs [SconscriptFilePath] [options]"
    print "Examples:"
    print "  snocs .. compiler=vc9 platform=x86 configuration=Debug" 
    print "  snocs test -Q           #build and run tests with reduced log" 
    print "  snocs install -c        #clean installation"
    print "SconscriptFilePath can be absolute, relative to current path, or "
    print "relative to projects root path e.g.:"
    print "  snocs github.com\osblinnikov\snocs\examples\helloWorld compiler=vc9 test"
    print "**********************"
    print "Available options:"
    print "  compiler={g++,mingw,vc9,vc10,vc11,vc11exp}"
    print "  configuration={Debug,Release}"
    print "  platform={x86,Win32,x64} # Win32 is an alias to x86"
    print "  verbose=1 # enables scons debug output"
    print "**********************"
    print "Other options could be SCons specific."
    print "  If you want to change default path to the Projects directory please see the"
    print "  builder.py file and PROJECTS_ROOT_PATH variable"
    print "  During 'test' phase snocs updates LD_LIBRARY_PATH local copy to provide"
    print "  of shared libraries"
    print "**********************"
    

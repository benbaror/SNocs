import os.path
import sys
from builder import *

args = prepare_args(ARGUMENTS)

env = Environment(
    BUILDERS = {'Test' :  Builder(action = builder_unit_test)},
    TOOLS  = args['TOOLS'],    
    TARGET_ARCH  = args['TARGET_ARCH'],
    MSVC_VERSION = args['MSVC_VERSION'],
    LIBPATH = args['LIBPATH'],
    LIBS = args['LIBS'],
    LINKFLAGS = args['LINKFLAGS'],
    CPPPATH = args['CPPPATH'],
    CPPDEFINES = args['CPPDEFINES'],
    CCFLAGS = args['CCFLAGS'],
    CCCOMSTR = args['CCCOMSTR'],
    LINKCOMSTR = args['LINKCOMSTR'],
    ENV = os.environ
)
env.AppendENVPath('LD_LIBRARY_PATH', Dir(args['INSTALL_PATH']).abspath)
env.AppendENVPath('PATH', Dir(args['INSTALL_PATH']).abspath)
                
Progress('Evaluating $TARGET\n')
env.Decider( 'MD5-timestamp' )          # For speed, use timestamps for change, followed by MD5
# Export this environment for use by the SConscript files
Export( 'env', 'args' )

#--------------------------------------
#           SOLUTION Builders
#--------------------------------------

args['SCONSCRIPT_PATH'] = os.path.abspath(os.path.dirname(args['SCONSCRIPT']))
args['BIN_DIR'] = os.path.join(args['SCONSCRIPT_PATH'], 'bin', args['configuration'])            
env.AppendENVPath('LD_LIBRARY_PATH', Dir(args['BIN_DIR']).abspath)
env.AppendENVPath('PATH', Dir(args['BIN_DIR']).abspath)
                
#start main build
print args['SCONSCRIPT']
SConscript( args['SCONSCRIPT'] )
#Include crossproject dependencies
dictLaunchedDependencies = {}
if args.get('CROSSPROJECT_DEPENDENCIES')!=None:
    foundNewDependency = 1
    while foundNewDependency == 1:
        foundNewDependency = 0
        for dep in args['CROSSPROJECT_DEPENDENCIES']:
            if args['CROSSPROJECT_DEPENDENCIES'][dep] not in dictLaunchedDependencies:
                foundNewDependency = 1
                args['SCONSCRIPT'] = os.path.join(args['CROSSPROJECT_DEPENDENCIES'][dep],'Sconscript')
                args['SCONSCRIPT_PATH'] = os.path.abspath(os.path.dirname(args['SCONSCRIPT']))
                args['BIN_DIR'] = os.path.join(args['SCONSCRIPT_PATH'], 'bin', args['configuration'])            
                env.AppendENVPath('LD_LIBRARY_PATH', Dir(args['BIN_DIR']).abspath)
                env.AppendENVPath('PATH', Dir(args['BIN_DIR']).abspath)
                #start building dependency
                print args['SCONSCRIPT']
                SConscript(args['SCONSCRIPT'])
                dictLaunchedDependencies[args['CROSSPROJECT_DEPENDENCIES'][dep]] = 1
                break
Alias('test', args['TEST_ALIASES'])#run env.Install when install command provided in command line
args['INSTALL_ALIASES'].append( args['TEST_ALIASES'] )
Alias('install', args['INSTALL_ALIASES'])#run env.Install when install command provided in command line
print "args['INSTALL_ALIASES'] size: "+str(len(args['INSTALL_ALIASES']))
print "args['TEST_ALIASES'] size: "+str(len(args['TEST_ALIASES']))
#--------------------------------------
#           Setting scons require()
#--------------------------------------
for prog in args['APP_DEPENDENCIES']:
    for dep in args['APP_DEPENDENCIES'][prog]:
        print prog+" depending on "+dep
        Requires(args['APP_BUILD'][prog], args['APP_BUILD'][dep])

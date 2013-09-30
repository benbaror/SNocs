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
env.AppendENVPath('LD_LIBRARY_PATH', Dir(os.path.join(args['INSTALL_PATH'],'lib')).abspath)
env.AppendENVPath('PATH', Dir(os.path.join(args['INSTALL_PATH'],'lib')).abspath)
                
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
if args['CLEANING_STAGE'] == '0':
    #Include crossproject dependencies
    dictLaunchedDependencies = {}
    if args.get('CROSSPROJECT_DEPENDENCIES')!=None:
        foundNewDependency = 1
        while foundNewDependency == 1:
            foundNewDependency = 0
            for depFullPath in args['CROSSPROJECT_DEPENDENCIES']:
                if depFullPath not in dictLaunchedDependencies:
                    foundNewDependency = 1
                    args['SCONSCRIPT'] = os.path.join(depFullPath,'SConscript')
                    args['SCONSCRIPT_PATH'] = os.path.abspath(os.path.dirname(args['SCONSCRIPT']))
                    args['BIN_DIR'] = os.path.join(args['SCONSCRIPT_PATH'], 'bin', args['configuration'])            
                    env.AppendENVPath('LD_LIBRARY_PATH', Dir(args['BIN_DIR']).abspath)
                    env.AppendENVPath('PATH', Dir(args['BIN_DIR']).abspath)
                    #start building dependency
                    print args['SCONSCRIPT']
                    SConscript(args['SCONSCRIPT'])
                    dictLaunchedDependencies[depFullPath] = 1
                    break
    #--------------------------------------
    #           Setting scons require()
    #--------------------------------------
    for prog in args['APP_DEPENDENCIES']:
        for dep in args['APP_DEPENDENCIES'][prog]:
            print prog+" depending on "+dep
            Requires(args['APP_BUILD'][prog], args['APP_BUILD'][dep])

Alias('test', args['TEST_ALIASES'])#run env.Install when install command provided in command line
args['INSTALL_ALIASES'].append( args['TEST_ALIASES'] )
Alias('install', args['INSTALL_ALIASES'])#run env.Install when install command provided in command line

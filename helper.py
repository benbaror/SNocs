import os.path
import shutil
#--------------------------------------
#            Functions
#--------------------------------------

# Prepends the full path information to the output directory so that the build
# files are dropped into the directory specified by trgt rather than in the 
# same directory as the SConscript file.
# 
# Parameters:
#   env     - The environment to assign the Program value for
#   outdir  - The relative path to the location you want the Program binary to be placed
#   trgt    - The target application name (without extension)
#   srcs    - The list of source files
# Ref:
#   Credit grieve and his local SCons guru for this: 
#   http://stackoverflow.com/questions/279860/how-do-i-get-projects-to-place-their-build-output-into-the-same-directory-with
def PrefixProgram(args, trgt, srcs):
    linkom = None
    if args['MSVC_VERSION'] != None and float(args['MSVC_VERSION'].translate(None, 'Exp')) < 11:
        linkom = 'mt.exe -nologo -manifest ${TARGET}.manifest -outputresource:$TARGET;1'
    if args['MSVC_PDB']:
        args['prj_env'].Append(PDB = os.path.join( args['BIN_DIR'], trgt + args['ARCHITECTURE_CODE'] + '.pdb' ))
    targetFullPath = os.path.join(args['SCONSCRIPT_PATH'],trgt + args['ARCHITECTURE_CODE'])
    args['APP_BUILD'][targetFullPath] = args['prj_env'].Program(
        target = os.path.join(args['BIN_DIR'], trgt + args['ARCHITECTURE_CODE']), 
        source = srcs, 
        LINKCOM  = [args['prj_env']['LINKCOM'], linkom]
    )
    args['INSTALL_ALIASES'].append(args['prj_env'].Install(os.path.join(args['INSTALL_PATH'],'bin'), args['APP_BUILD'][targetFullPath]))#setup install directory

    return args['APP_BUILD'][targetFullPath]

def PrefixTest(args, trgt, srcs):
    linkom = None
    if args['MSVC_VERSION'] != None and float(args['MSVC_VERSION'].translate(None, 'Exp')) < 11:
        linkom = 'mt.exe -nologo -manifest ${TARGET}.manifest -outputresource:$TARGET;1'
    if args['MSVC_PDB']:
        args['prj_env'].Append(PDB = os.path.join( args['BIN_DIR'], trgt + args['ARCHITECTURE_CODE'] + '.pdb' ))
    targetFullPath = os.path.join(args['SCONSCRIPT_PATH'],trgt + args['ARCHITECTURE_CODE'])
    args['APP_BUILD'][targetFullPath] = args['prj_env'].Program(target = os.path.join(args['BIN_DIR'], trgt+args['ARCHITECTURE_CODE']), source = srcs, LINKCOM  = [args['prj_env']['LINKCOM'], linkom])
    args['INSTALL_ALIASES'].append(args['prj_env'].Install(os.path.join(args['INSTALL_PATH'],'bin'), args['APP_BUILD'][targetFullPath]))#setup install directory

    testPassedFullPath = os.path.join(args['SCONSCRIPT_PATH'],args['PassedTestsOutputFileName'])
    args['TEST_ALIASES'].append(args['prj_env'].Test(testPassedFullPath, args['APP_BUILD'][targetFullPath]))

    return args['APP_BUILD'][targetFullPath]

# Similar to PrefixProgram above, except for Library
def PrefixLibrary(args, trgt, srcs):
    if args['MSVC_PDB']:
        args['prj_env'].Append(PDB = os.path.join( args['LIB_DIR'], trgt+args['ARCHITECTURE_CODE'] + '.pdb' ))
    targetFullPath = os.path.join(args['SCONSCRIPT_PATH'],trgt+args['ARCHITECTURE_CODE'])
    args['APP_BUILD'][targetFullPath] = args['prj_env'].Library(target = os.path.join(args['LIB_DIR'], trgt+args['ARCHITECTURE_CODE']), source = srcs)
    args['INSTALL_ALIASES'].append(args['prj_env'].Install(os.path.join(args['INSTALL_PATH'],'lib'), args['APP_BUILD'][targetFullPath]))#setup install directory
    return args['APP_BUILD'][targetFullPath]
    
# Similar to PrefixProgram above, except for SharedLibrary
def PrefixSharedLibrary(args, trgt, srcs):
    linkom = None
    if args['MSVC_VERSION'] != None and float(args['MSVC_VERSION'].translate(None, 'Exp')) < 11:
        linkom = 'mt.exe -nologo -manifest ${TARGET}.manifest -outputresource:$TARGET;2'
    if args['MSVC_PDB']:
        args['prj_env'].Append(PDB = os.path.join( args['LIB_DIR'], trgt+args['ARCHITECTURE_CODE'] + '.pdb' ))
    targetFullPath = os.path.join(args['SCONSCRIPT_PATH'],trgt+args['ARCHITECTURE_CODE'])
    args['APP_BUILD'][targetFullPath] = args['prj_env'].SharedLibrary(target = os.path.join(args['LIB_DIR'], trgt+args['ARCHITECTURE_CODE']), source = srcs, LINKCOM  = [args['prj_env']['LINKCOM'], linkom]) 
    args['INSTALL_ALIASES'].append(args['prj_env'].Install(os.path.join(args['INSTALL_PATH'],'lib'), args['APP_BUILD'][targetFullPath]))#setup install directory
    return args['APP_BUILD'][targetFullPath]

def PrefixFilename(filename, extensions):
    return [(filename + ext) for ext in extensions]

# Prefix the source files names with the source directory
def PrefixSources(args, srcdir, srcs):
    return  [os.path.join(args['SCONSCRIPT_PATH'],srcdir, x) for x in srcs]

def AddDependencyPc(args, prog, dep, deppath):
    if deppath != None:
        args['prj_env'].AppendENVPath('PKG_CONFIG_PATH', [deppath])
        args['prj_env'].ParseConfig('pkg-config'+
            ' --define-variable=prefix='+deppath+' --define-variable=configuration='+args['configuration']+
            ' --define-variable=architecture_code='+args['ARCHITECTURE_CODE']+
            ' --print-errors  --cflags --libs '+dep
        )
        args['prj_env'].Append(LIBPATH = [' `pkg-config --define-variable=prefix='+deppath+' --variable=libdir '+dep+'` '])
    else:
        args['prj_env'].ParseConfig('pkg-config'+
            ' --define-variable=configuration='+args['configuration']+
            ' --define-variable=architecture_code='+args['ARCHITECTURE_CODE']+
            ' --print-errors  --cflags --libs '+dep
        )
        args['prj_env'].Append(LIBPATH = [' `pkg-config --variable=libdir '+dep+'` '])

def AddDependency(args, prog, dep, deppath):
    AddOrdering(args,prog,dep,deppath)
    AddDependencyPc(args,prog, dep, deppath)
    
def AddOrdering(args, prog, dep, deppath):
    prog = os.path.join(args['SCONSCRIPT_PATH'],prog+args['ARCHITECTURE_CODE'])
    if args['APP_DEPENDENCIES'].get(prog) == None:
        args['APP_DEPENDENCIES'][prog] = [];
    depFullPath = os.path.join(deppath,dep+args['ARCHITECTURE_CODE'])
    args['APP_DEPENDENCIES'][prog].append(depFullPath)
    if deppath != args['SCONSCRIPT_PATH']:
        if args.get('CROSSPROJECT_DEPENDENCIES') == None:
            args['CROSSPROJECT_DEPENDENCIES'] = {};
        if args['CROSSPROJECT_DEPENDENCIES'].get(deppath) == None:
            args['CROSSPROJECT_DEPENDENCIES'][deppath] = dep
            
def AddScript(args, dep, deppath):
    if deppath != args['SCONSCRIPT_PATH']:
        if args.get('CROSSPROJECT_DEPENDENCIES') == None:
            args['CROSSPROJECT_DEPENDENCIES'] = {};
        if args['CROSSPROJECT_DEPENDENCIES'].get(deppath) == None:
            args['CROSSPROJECT_DEPENDENCIES'][deppath] = dep
            
def AddPthreads(env, args):
    PATH_TO_PTHREADS_WIN = os.path.join(args['PROJECTS_SRC_PATH'],'sourceware.org','pthreads-win32','dll-latest')
    if args['MSVC_VERSION'] != None:
        args['prj_env'].Append(
            LIBS = ['pthreadVC2'],
            CPPPATH = [os.path.join(PATH_TO_PTHREADS_WIN,'include')],
            LIBPATH = [os.path.join(PATH_TO_PTHREADS_WIN,'lib',args['TARGET_ARCH'])]
        )
        env.AppendENVPath('PATH', os.path.join(PATH_TO_PTHREADS_WIN,'dll',args['TARGET_ARCH']))
    elif args['COMPILER_CODE'] == 'mingw':
        args['prj_env'].Append(
            LIBS = ['pthreadGC2'],
            CPPPATH = [os.path.join(PATH_TO_PTHREADS_WIN,'include')],
            LIBPATH = [os.path.join(PATH_TO_PTHREADS_WIN,'lib',args['TARGET_ARCH'])]
        )
        env.AppendENVPath('PATH', os.path.join(PATH_TO_PTHREADS_WIN,'dll',args['TARGET_ARCH']))
    else:
        args['prj_env'].Append(LIBS = ['pthread'])
    

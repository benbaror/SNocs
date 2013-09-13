#ifdef T
#include "template.h"

#ifndef SnocsTemplateExportsAPI
#if defined WIN32 && !defined __MINGW32__ && !defined(CYGWIN)
    #ifdef SnocsTemplateExports
        #define SnocsTemplateExportsAPI __declspec(dllexport)
    #else
        #define SnocsTemplateExportsAPI __declspec(dllimport)
    #endif
#else
    #define SnocsTemplateExportsAPI extern
#endif
#endif

SnocsTemplateExportsAPI void TEMPLATE(sum,T) (int n, T *a, T *b);

#endif
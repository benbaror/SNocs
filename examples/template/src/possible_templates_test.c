#include "template.h"
#include "possible_templates_test.h"

#ifdef T
#undef T
#endif
#define T float
#include "templates_test.c"

#ifdef T
#undef T
#endif
#define T double
#include "templates_test.c"

#ifdef T
#undef T
#endif
#define T int
#include "templates_test.c"
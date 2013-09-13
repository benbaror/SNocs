#ifndef ALL_POSSIBLE_SUMS_H_ 
#define ALL_POSSIBLE_SUMS_H_ 

#include "template.h"

#ifdef T
#undef T
#endif
#define T float
#include "templates_test.h"

#ifdef T
#undef T
#endif
#define T double
#include "templates_test.h"

#ifdef T
#undef T
#endif
#define T int
#include "templates_test.h"

#endif
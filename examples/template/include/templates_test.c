#ifdef T

#include "template.h"

void TEMPLATE(sum,T) (int n, T *a, T *b)
{
    /* computes a:=a+b where a and b are two arrays of length n */
    int i;
    for(i=0;i<n;i++) a[i]+=b[i];
}

#endif
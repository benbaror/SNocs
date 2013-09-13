#include "possible_templates_test.h"
#include <stdio.h>

int main(int argc, char **argv){
    printf("------possible_templates_test_main---\n");
    int ai[3];
    ai[0] = 1; ai[1] = 2; ai[2] = 3;
    int bi[3];
    bi[0] = 4; bi[1] = 5; bi[2] = 6;
    
    float af[3] = {1.0,2.0,3.0};
    float bf[3] = {1.5,2.5,3.5};
    TEMPLATE(sum,int)(3,ai,bi);
    TEMPLATE(sum,float)(3,af,bf);
    printf("af[0]=%f, ai[0]=%d\n",af[0],ai[0]);
    return 0;
}
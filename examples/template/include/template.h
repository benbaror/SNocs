#ifndef AIRUCORE_TEMPLATES_H
#define AIRUCORE_TEMPLATES_H

//with single potential parameter for template
#define TEMPLATE_CAT(X,Y) X##_##Y
#define TEMPLATE(X,Y) TEMPLATE_CAT(X,Y)

//With two potential parameters for template
#define TEMPLATE2_CAT(X,Y,Z) X##_##Y##_##Z
#define TEMPLATE2(X,Y,Z) TEMPLATE2_CAT(X,Y,Z)

#endif//AIRUCORE_TEMPLATES_H
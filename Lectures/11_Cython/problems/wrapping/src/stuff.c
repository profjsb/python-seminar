#include <math.h>

#include "stuff.h"

void compute(int n, double *in, double *out)
{
    int j;
    for (j = 0; j < n; ++j) {
        out[j] = sin(in[j]);
    }
}

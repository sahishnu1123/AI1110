#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"coeffs.h"

int main (void)
{
//mean of uniform
printf("mean = %lf\n",mean("gau.dat"));

//variene of uniform
printf("varience = %lf\n",varience("gau.dat"));
}

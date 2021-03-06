/**
 * If we list all the natural numbers below 10 that are multiples of
 * 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * 
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */

#include <stdio.h>

int main(void)
{
    printf("%d\n",
           (3 * (999 / 3) * (999 / 3 + 1) + 5 * (999 / 5) * (999 / 5 + 1) - 15 * (999 / 15) * (999 / 15 + 1)) / 2);
    return 0;
}

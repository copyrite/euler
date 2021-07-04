/**
 * A palindromic number reads the same both ways. The largest palindrome made
 * from the product of two 2-digit numbers is 9009 = 91 * 99.
 * 
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */

#include <stdio.h>
#include "palindrome.h"

int main(void)
{
    unsigned int x, y, candidate, best;
    char str[7];

    best = 0;
    for (x = 990; x > 99; x -= 11)
    {
        /* Maximum can't be exceeded globally anymore; exit loop and terminate */
        candidate = 999 * x;
        if (candidate < best)
        {
            break;
        }

        for (y = 999; y > 99; --y)
        {
            candidate = x * y;

            /* Maximum can't be exceeded in this block anymore; exit loop early */
            if (candidate <= best)
            {
                break;
            }

            sprintf(str, "%u", candidate);
            if (strpal(str))
            {
                best = candidate;
                /* New maximum found, exit loop */
                break;
            }
        }
    }

    printf("%d\n", best);

    return 0;
}
/**
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * 
 * What is the largest prime factor of the number 600851475143 ?
 */

#include <stdio.h>
#include <gmp.h>

int main(void)
{
    mpz_t quotient, remainder, dividend, divisor, divisor_sq;
    unsigned short i, x[8] = {6, 4, 2, 4, 2, 4, 6, 2};

    mpz_init(quotient);
    mpz_init(remainder);
    mpz_init_set_str(dividend, "600851475143", 10);
    mpz_init_set_ui(divisor, 2);
    mpz_init_set_ui(divisor_sq, 4);

    /* Small divisors 2, 3, 5 */
    for (i = 0; i < 3; ++i)
    {
        while (mpz_cmp(divisor_sq, dividend) <= 0)
        {
            mpz_fdiv_qr(quotient, remainder, dividend, divisor);
            if (mpz_cmp_ui(remainder, 0) == 0)
            {
                mpz_set(dividend, quotient);
            }
            else
            {
                break;
            }
        }
        mpz_add_ui(divisor, divisor, i + 1);
        mpz_pow_ui(divisor_sq, divisor, 2);
    }

    /* Divisors 7 and greater */
    mpz_set_ui(divisor, 7);
    mpz_pow_ui(divisor_sq, divisor, 2);
    i = 0;
    while (mpz_cmp(divisor_sq, dividend) <= 0)
    {
        mpz_fdiv_qr(quotient, remainder, dividend, divisor);
        if (mpz_cmp_ui(remainder, 0) == 0)
        {
            mpz_set(dividend, quotient);
        }
        else
        {
            i = (i + 1) % 8;
            mpz_add_ui(divisor, divisor, x[i]);
            mpz_pow_ui(divisor_sq, divisor, 2);
        }
    }

    gmp_printf("%Zd\n", dividend);

    mpz_clear(quotient);
    mpz_clear(remainder);
    mpz_clear(dividend);
    mpz_clear(divisor);
    mpz_clear(divisor_sq);

    return 0;
}

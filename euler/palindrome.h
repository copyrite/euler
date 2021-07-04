#include <string.h>

int strpal(char *str)
{
    size_t i, n;
    n = strlen(str);
    for (i = 0; i < n / 2; ++i)
    {
        if (str[i] != str[n - i - 1])
        {
            return 0;
        }
    }
    return 1;
}

#include <stdio.h>
#include <stdlib.h>
int num, divisor;
int alist[100000000];

int main(void)
{
    // read the first line
    scanf("%d %d", &num, &divisor);

    // use for loop to read the second line
    // Divide the list with the divisor
    for (int i = 0; i < num; i++)
    {
        scanf("%d", &alist[i]);
        alist[i] = alist[i] / divisor;
    }

    // Find duplicate values and their number of occurence, assign it to a dictionary

    return 0;
}
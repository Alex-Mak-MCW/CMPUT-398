// Impossible criteria: more 2 than 1's/ 2 the wrong thing
// queue: the thing you remove is the always the first thing
// Pqueue: the thing you remove is the largest in the list
// Stack: the thing you remove is the last item in the list
// Not sure: both priority queue and queue

// list for commands, list for all the 1's, list for all the 2's

#include <stdio.h>
int alist[1000];
int blist[1000];
int main(void)
{
    int num;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d %d", &alist[i], &blist[i]);
    }
    for (int i = 0; i < num; i++)
    {
        printf("%d\n", alist[i]);
    }
    printf("empty");
    for (int i = 0; i < num; i++)
    {
        printf("%d\n", blist[i]);
    }
    // check impossible
    if (/* condition */)
    {
        /* code */
    }
}
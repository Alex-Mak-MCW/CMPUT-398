import math

# Perform Recursive Binary Search, learned back in CMPUT 175
# Role: To search the index where the number is equal/ slightly less than the total maximum, then return the extra
def binary_search(low,high,number,extra):

    # Find the middle index of the list
    mid = (low+high)//2

    # Avoid scenario where high is less than low, when the search completes
    if high >= low:
        # Base case of recursion: if found exact number, return 0 as no surplus
        if number == n[mid]:
            return 0
        # Find surplus part
        # if the difference between list/sublist's middle elment and the number we look for is still less than extra, and not negtive
        # then total_extra will be the absolute value of the difference between the 
        # use absolute function incase the difference is negative
        if (n[mid]-number) < extra and (n[mid] - number >= 0):
            extra = abs(number-n[mid])

        # Recursive part to perfrom binary search in n's sublist
        if number > n[mid]:
            # print("1")
            return binary_search(mid+1, high, number, extra)
        else:
            # print("2")
            return binary_search(low, mid-1, number, extra)
    return extra

# declare lists as global so binary search function can use
n=[]
m=[]

def main():
    # Read input and assign values from input
    first=[]
    first.append(input().split())

    for i in range (int(first[0][0])):
        n.append(int(input()))
    for i in range (int(first[0][1])):
        m.append(int(input()))

    # Sort the lists in ascending order to perfrom binary search
    n.sort() # [5,7,9]
    m.sort() # [6,8]

    total = 0
    # Get the sum the maximum values in both lists 
    total_max = max(n) + max(m)

    # iterate through m, for each element perform binary search to get the surplius for each element in m
    for x in m:
        total += (binary_search(0,len(n)-1,x,total_max))
    print(total)
main()
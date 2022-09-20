"""
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  - N/A

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I did not discuss with anyone for this problem.

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
# Perform Recursive Binary Search, learned back in CMPUT 175
# Role: To search the index where the number is equal/ slightly less than the total maximum, then return the extra
# extra is the total surplus of all colors
def binary_search(low,high,number, extra):

    # Find the middle index of the list
    mid = (low+high)//2

    # Avoid scenario where high is less than low, when the search completes
    if high >= low:
        # Base case of recursion: if found exact number, return 0 as no surplus
        if number == n[mid]:
            return 0
        # Find surplus part for each color
        # if the list/sublist's middle elment is larger than the number we are looking for
        # then extra will be the absolute value of the difference between the 
        if  n[mid] - number >= 0:
            extra = n[mid] - number

        # Recursive part to perfrom binary search in n's sublist
        if number > n[mid]:
            return binary_search(mid+1, high, number, extra)
        else:
            return binary_search(low, mid-1, number, extra)
    return extra

# Declare lists as global so binary search function can use
n=[]
m=[]

def main():
    # Read input and assign values from input
    first=[]
    first.append(input().split())
    total = 0

    for i in range (int(first[0][0])):
        n.append(int(input()))
    for i in range (int(first[0][1])):
        m.append(int(input()))

    # Sort the lists in ascending order to perfrom binary search
    n.sort()
    m.sort()

    # Iterate through m, for each element perform binary search to get the surplius for each element in m
    for x in m:
        total += (binary_search(0,len(n)-1,x,0))
    print(total)
main()
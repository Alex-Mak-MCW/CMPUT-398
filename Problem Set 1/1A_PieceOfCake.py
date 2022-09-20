"""
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  # - https://blog.finxter.com/how-to-convert-a-string-list-to-an-integer-list-in-python/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I did not discuss with anyone for this problem.

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
# Import math library to compute the product of a list
import math

# read the input and split them into list item, assign it to a list
alist=input().split(" ")

# Map the original list from a list of strings to list of integers, link referenced in the header
# I have learned from the link below to convert a list of string to a list of intergers using the map method
# https://blog.finxter.com/how-to-convert-a-string-list-to-an-integer-list-in-python/
alist=list(map(int,alist))

# Use for loop to update list element
# Use the enumerate method, i as counter, n as list element, skip the first element of the list
for i,n in enumerate(alist[1:]):
    if n<alist[0]/2:
        alist[i+1]=alist[0]-n
# Compute the output, volume= length * width * height, height is deualt as 4
print(math.prod(alist[1:])*4)

# input: n, h, v
# n=4
# h=2
# v=1

# if h<=n/2:
#    h=n-h
# if v<=n/2:
#     v=n-v
# print(h*v*4)

# alist=[10,4,7]
# Volume= length * width * 4 (height)
# Read the 3 number (digit by digit), as list?
# If the second/ third one is less than half of first, minus it out
# else keep it as it is
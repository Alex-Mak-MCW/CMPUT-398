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
lines=[]
# Read the 2-line input, and append it to a list
for i in range(2):
    lines.append(input().split(" "))

# Map the original list from a list of strings to list of integers, link referenced in the header
# I have learned from the link below to convert a list of string to a list of intergers using the map method
# Notes: I have reapplied this concept that I used in problem 1A, PieceOfCake.py
# https://blog.finxter.com/how-to-convert-a-string-list-to-an-integer-list-in-python/
# Assign input to variables
lines[1]=list(map(int,lines[1]))
# divisor=int(lines[0][1])
# alist=lines[1]
total=0
# Use for loop with numerate to traverse list with a counter; i=counter and n= list element
# Compare the list elements with the succeeding value (righter values)
for i,n in enumerate(lines[1]):
    left=n//int(lines[0][1])
    blist=[]
    for j in range(len(lines[1][i+1:])):
        right=lines[1][j]//int(lines[0][1])
        # If the quotient has not existed before, append it to a list
        if right not in blist:
            blist.append(right)
        # If the quotient has existed before, increment the distinct pair value
        else:
            total+=1
print(total)
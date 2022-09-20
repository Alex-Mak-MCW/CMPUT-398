"""
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  - https://www.w3schools.com/python/ref_list_count.asp

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I have discussed this problem with Jayden Cho

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
import time
start=time.time()

lines=[]
# Read the 2-line input, and append it to a list
for i in range(2):
    lines.append(input().split(" "))
    
dup={}
result=0
# Divide the list with the divisor
for i,n in enumerate(lines[1]):
    lines[1][i]=int(n)//int(lines[0][1])

# Find duplicate values and their number of occurence, assign it to a dictionary
# I have learned online using the count method, through the link below
# https://www.w3schools.com/python/ref_list_count.asp
for i in lines[1]:
    j=lines[1].count(i)
    # If there's more than 1 occurence
    if j>1:
        dup[i]=j
print(dup)

# Compute the combination of pairs in a for loop through iterating the duplicate item dictionary
for key,value in dup.items():
    result+=value*(value-1)//2
print(result)

print(time.time()-start)
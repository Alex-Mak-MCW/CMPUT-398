"""
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  - https://www.programiz.com/python-programming/methods/string/isnumeric

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I did not discuss with anyone for this problem.

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""

#       0   1   2       3       4       5       6
txt1="7\nBo\nPat\nJean\nKevin\nClaude\nWilliam\nMarybeth"
#       0      1    2   3       4       5
txt2="6\nJim\nBen\nZoe\nJoey\nFrederick\nAnnabelle"
txt3="5\nJohn\nBill\nFran\nStan\nCece"
# txt=input()
# alist=txt3.splitlines()

# Reading multiple line input using a while loop and a counter, assign the values in a 2d list, each list element is a list (so list of list)
i=0
alist=[[]]
while True:
    line=input()
    if line=="0":
        break
    # Used the isnumeric method to check whether the string input is a number or not, I have refreshed my knowledge using the link below
    # https://www.programiz.com/python-programming/methods/string/isnumeric
    if line.isnumeric():
        i+=1
        alist.append([line])
    else:
        alist[i].append(line)

# Due to the implciation above, there is extra empty list in the beginning of the list, remove it
alist.remove([])

# Use for loop to traverse 2d list and reassign list element
for j in range(len(alist[1:])+1):
    # Inner for loop to traverse each list items (which is also a list)
    # i is counter, n is element
    for i,n in enumerate(alist[j][1:]):
        # reassign the inner list's element based on the index (odd/even)
        if i%2==0:
            alist[j][i//2+1]=n
        else:
            alist[j][int(alist[j][0])-i//2]=n

    # Print the Results excpet the number in front using for loop
    print("SET "+str(j+1))
    for item in alist[j][1:]:
        print(item)

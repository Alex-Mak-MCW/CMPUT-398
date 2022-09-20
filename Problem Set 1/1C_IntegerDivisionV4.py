"""
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  - https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user 
  - https://discuss.codechef.com/t/formula-n-n-1-2/9774/3

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I have discussed this problem with Jayden Cho

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
def main():
    result=0
    adict={}
    # Read only the second digit, since I can iterate the second line as a list, no need to read the first digit in the first line
    divisor=int(input().split()[1])
    # Use the map method to map read items (second line of input) in integer types (numbers)
    # Then use for loop to traverse that integer list
    # I have learned from the link below:
    # https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user 
    for i in map(int,input().split()):

        # Perform interger divison on each list element, then assign the number of occurence on the dictionary
        # If the dicitionary already has the key(meaning the quotient has appeared before), increment that key's value by 1
        # Otherise create a new item with the value of 1
        if i//divisor in adict:
            adict[i//divisor]+=1
        else:
            adict[i//divisor]=1
    
    # Use for loop to iterate dictionary
    for key,value in adict.items():
        # For all the quotients that have occured more than once, use the combination formula to determine the total number of distinct pairs.
        if value!=1:
            # combination formula: n chooses r, which can also use the formula (n*(n-1)/2), r always equals to 2
            # I have learned from the link below
            # https://discuss.codechef.com/t/formula-n-n-1-2/9774/3
            result+=value*(value-1)//2
    print(result)
main()
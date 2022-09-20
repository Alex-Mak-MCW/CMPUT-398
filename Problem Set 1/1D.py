# First part of the conversion
# Function from alien language to integer, takes key and message
def source_to_int(key, message):

    # intialize variables
    adict={}
    # assign a integer to each character to an integer sequentially, done by mapping values in a dictionary through a for loop
    for i in range(len(message)):
        adict[message[i]]=i

    int_result=0
    n=0
    # use reversed to reverse the string, for each character of the string
    for i in reversed(key):
        # the integer result will be incremented by the proudct of the dictionary's values, and the source language's length^n, which n is the inceasing power for every iteration in the for loop
        int_result += adict[i] * pow(len(message), n)
        n += 1
    return int_result

# Second part of the conversion
# From code back to target language, int result= code we get from base_to_int function, lang is the target language
def int_to_target(int_result, target):
    length=len(target)
    bdict={}
    blist = []
    # assign a character iteratively in numbers, opposite of the first method
    for i in range(length):
        bdict[i]=target[i]
    print(bdict)

    # revert the changes made in the previous method, source_to_int
    while int_result > 0:
        result=int_result % length
        temp=bdict[result]
        int_result //= length
        blist = [temp] + blist

    # join the list elemetns into a string, then return it
    target_string="".join(blist)
    return target_string


def main():
    # Read the inputs
    lines=[]
    for i in range(int(input())):
        lines.append(input().split(" "))

    # For each test case, print output
    for i in range(len(lines)):
        conv_to_int=source_to_int(lines[i][0], lines[i][1])
        target=int_to_target(conv_to_int,lines[i][2])
        print("Case #{0}: {1}".format(i+1, target))
main()

"""
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  - https://realpython.com/python-eval-function/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I did not discuss with anyone for this problem.

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""

import sys

def main():
    # dictionary that stores the word as the key; number as its value
    word_to_int={}
    # dictionary that stores the number as its keys; word as its values
    int_to_word={}

    # for each line of user's input
    for line in sys.stdin:
        # Clean up the input line to make sure nothing extra is recorded, only read after the command
        # original_str only use when printing a successful calculation/ or unknown message
        original_str=line.strip()[5:len(line)]
        # split line into list elements for checking later
        line=line.split()
        # target_str stores the final math expression for the eval function below
        target_str=""
        # bool to check whether need to print
        calculate=True

        # for non-empty input lines
        if len(line)>0:
            # If it's a define command, update both dictionaries
            if line[0]=="def":
                # If the word is already in the word_to_int dict before, deletes the word from word_to_dict for new update below
                if line[1] in word_to_int.keys():
                    word=word_to_int[line[1]]
                    del int_to_word[word]
                #stores the new value back to both dictionaries  
                word_to_int[line[1]] = line[2] 
                int_to_word[line[2]] = line[1]

            # If it's a calculate command
            elif line[0]=="calc":
                # iterate through each word/ string from the line except the first one:
                for each in line[1:len(line)-1]:
                    # if the word is in the word to int dictionary, then it's an existing word and concatenate to the target string
                    if each in word_to_int:
                        target_str+=str(word_to_int[each])
                    # if it is a add/subtract sign, still add that sign to the string
                    elif each == "+" or each=="-":
                        target_str+=each
                    # adding a new word, don't add to the target string
                    else:
                        print(original_str+" unknown")
                        calculate=False
                        break
                
                # Use the eval method to compute the numerical result
                if calculate:
                    # I have learned how to use the eval fucntion from python to print numerical result based on string expression, using the link below:
                    # https://realpython.com/python-eval-function/
                    ans=str(eval(target_str))
                    # if the answer's value has a known word, print the word else print unknown
                    if ans in int_to_word:
                        print(original_str+" "+int_to_word[ans])
                    else:
                        print(original_str+" unknown")
            
            # If it's a clear command
            elif line[0]=="clear":
                # Reset both dictionaries using the clear method, I have learned from the link below:
                word_to_int.clear()
                int_to_word.clear()
main()
"""
Whenever the definition of variables was given I stored it in 'words' dictionary and its reverse in the 'reverse' dictionary. 
When the new update of the variable was given I deleted it from the reverse dictionary if it is already present in the key of words dictionary and then updated both dictionaries.
When the calc expression was given I converted it into the mathematical expression by removing the keywords and equal sign from it. 
Then I evaluated the expression using the eval() function. After that, I check whether the result value is present in the reverse dictionary or not. 
Then accordingly printed the result. If clear keywords were given then I cleared both dictionaries. The program code for the kattis adding words solution in python is given below.
"""

import sys

def main():
    # dictionary that stores the word as the key; number as its value
    word_to_int={}
    # dictionary that stores the number as its keys; word as its values
    int_to_word={}

    # for each line of input
    for line in sys.stdin:
        # Clean up the input line to make sure nothing extra is recorded, only read after the command
        # original_str only use when using the calc command
        orginal_str=line.strip()[5:len(line)]

        # split line into list elements for checking later
        line=line.split()
        # cal_string stores the final math expression for the eval function below
        target_str=""
        # bool to check whether need to print
        calculate=True

        # for non-empty input lines
        if len(line)>0:
            # If it's a define command, update both dictionaries
            if line[0]=="def":
                # If it's already here before, deletes the value in reverse upon the updation
                # if line[1] in word_to_int.keys():
                #     del int_to_word[word_to_int[line[1]]]
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
                        print(orginal_str,'unknown')
                        calculate=False
                        break
                
                # Use the eval method to compute the numerical result
                if calculate:
                    # https://realpython.com/python-eval-function/
                    ans=eval(cal_string)
                    if str(ans) in int_to_word:
                        print(orginal_str,int_to_word[str(ans)])
                    else:
                        print(orginal_str,'unknown')
            
            # If it's a clear command
            elif line[0]=="clear":
                # use the clear method to remove all items in both dictionaries
                word_to_int.clear()
                int_to_word.clear()
main()
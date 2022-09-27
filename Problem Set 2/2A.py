"""
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  I didn't use any resources for this problem.

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I did not discuss with any classmates for this problem.

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""

# use import sys to read each line's inputs using sys.stdin
import sys

def main():
    # Brute force approach, do the actual add and remove for every single possible data structure 
    q_list=[]
    p_list=[]
    s_list=[]
    items=0
    possible=queue=p_queue=stack=True
    
    for each_line in sys.stdin:
        # Prevent reading the last line with the empty "\n"
        if each_line=="\n":
            break
        # reading inputs, if  only 1 number, store it
        if " " not in each_line:
            items=int(each_line)
        else:
            temp=each_line.split(" ")
            # Temp 0 is command (add or remove), temp 1 is the value
            num=int(temp[1])
            if int(temp[0])==1:
                q_list.append(num)
                p_list.append(num)
                s_list.append(num)
                items-=1
            else:
                # If popping something that is not in any of these 3 list, then it's not possible
                if (num not in q_list) and (num not in p_list) and (num not in s_list):
                    possible=False
                else:
                    # Check queue
                    # Fail condition: If the queue list's first item is NOT the removed number, then it can't be a queue
                    if queue:
                        if q_list.pop(0)!=num:
                            queue=False
                    # Check Priority Queue
                    # Fail condition: if the priority queue list's largets item is NOT the removed number, then it can't be a priority queue
                    # Otherwise, remove that element from the list
                    if p_queue:
                        if max(p_list)!= num:
                            p_queue=False
                        else:
                            p_list.remove(num)
                    # Check Stack (LIFO)
                    # Fail condition: if the stack list's last item is NOT the removed number, then it can't be a stack
                    # Otherwise, remove that element from the list
                    if stack:
                        if s_list[-1]!=num:
                            stack=False
                        else:
                            s_list.pop()
                items-=1
    # Print the results when all the commands are executed
        if items==0:
            if not possible or (not stack and not p_queue and not queue):
                print("impossible")
            # not sure condition: when 
            elif (stack and p_queue) or (stack and queue) or (p_queue and queue):
                print("not sure")
            elif stack:
                print("stack")
            elif p_queue:
                print("priority queue")
            elif queue:
                print("queue")

            # Reset initialized variables for reiteration
            q_list=[]
            p_list=[]
            s_list=[]
            possible=queue=p_queue=stack=True
main()


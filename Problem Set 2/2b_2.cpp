/*
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  I have used the link below to learn more about the deque object in c++, especially its related methods like push/pop at back/front, as well as index locate methods like front/back
  - https://cplusplus.com/reference/deque/deque/

  I have used the link below to learn more about using the ceiling and floor fucntion in c++:
  - https://www.geeksforgeeks.org/ceil-floor-functions-cpp/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I didn't collaborate with anyone for this problem.

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
*/
#include <bits/stdc++.h>
#include <algorithm>
#include <iostream>
#include <deque>
#include <cmath>
#include <cstdlib>
#include <cstdio>
using namespace std;

int main()
{
    int lines;
    // read the input once for lines
    cin >> lines;

    // Use the 2 deque object to make a teque because it doesn't support insertion in the middle
    // q1 is the first half of the queue; q2 is the latter half of the queue
    deque<int> q1;
    deque<int> q2;

    // size 12 because the longest possible command is 11 (push_middle)

    for (int i = 0; i < lines; i++)
    {
        string str;
        int num;

        // Read inputs
        // (void)scanf("%s %d", command, &num);
        cin >> str >> num;
        // If the command is a get command, print the output and the next line char
        if (str == "get")
        {
            if (num < q1.size())
            {
                // prints the element from the first half queue and the newline character
                cout << q1[num] << '\n';
            }
            else
            {
                // prints the element from the latter half queue and the newline character
                // to find the proper index, use the overall index minus the total size of the left queue
                cout << q2[num - q1.size()] << '\n';
            }
        }
        // For the push_... methods:
        // if command is push_back, push num at the back of queue 2 (end of the whole queue):
        else if (str == "push_back")
        {
            q2.push_back(num);

            // Resizing both queues part, do this after push/pop happened:
            // if the right half of the queue is larger than the left half:
            // Pop front of the right half queue and push it to the end of the left half queue
            if (q2.size() > q1.size())
            {
                int temp = q2.front();
                q2.pop_front();
                q1.push_back(temp);
            }
        }
        // if command is push_front, push num at the front of queue 1 (front of the whole queue)
        else if (str == "push_front")
        {
            q1.push_front(num);
            // Resize part:
            // If the difference of the 2 queues is within 1 (right queue is 1 larger than the left queue), don't do anything
            // But if the left queue is more than 1 larger than the right queue:
            // Pop back of the left half queue and push it to the front of the right half queue
            // repeat same but opposite from the if statement above
            if ((q1.size() - q2.size()) > 1)
            {
                int temp = q1.back();
                q1.pop_back();
                q2.push_front(temp);
            }
        }
        // if command is push_middle, push num at the back of queue 1 (between the 2 queues/ back of the first queue)
        else if (str == "push_middle")
        {
            // If left queue is larget than right queue, add to the right queue to balance it ouy
            if (q1.size() > q2.size())
            {
                q2.push_front(num);
            }
            // opposite applies from above
            else
            {
                q1.push_back(num);
            }
        }
    }
}

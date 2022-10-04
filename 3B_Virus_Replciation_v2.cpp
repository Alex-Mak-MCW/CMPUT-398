/*
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  - https://cplusplus.com/reference/list/list/
  I have provided the reasonings to refrence each link over each comment

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I didn't collaborate with anyone for this problem.

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
*/
// #include <bits/stdc++.h>
#include <iostream>
#include <list>

using namespace std;

int main()
{
    list<char> alist, blist;

    // Read character by character, stop until the newline character
    // Do this twice from both lines and both lists

    // I have used the link below to learn more about list methods in c++, like front, back, push/pop front/back
    // https://cplusplus.com/reference/list/list/
    char c;
    while (cin.get(c) && c != '\n')
    {
        alist.push_back(c);
    }
    while (cin.get(c) && c != '\n')
    {
        blist.push_back(c);
    }

    // Brute Force Approach :
    // If alist and blist has the same element from the same index, remove that index's element out
    // Whatever's left after the removing on the second list, its length is the answer we look for

    // For the front of both list, pop the ones that exist in both lists during same index
    while (!alist.empty() && !blist.empty() && (alist.front() == blist.front()))
    {
        alist.pop_front();
        blist.pop_front();
    }
    // same thing for the back of both list
    while (!alist.empty() && !blist.empty() && (alist.back() == blist.back()))
    {
        alist.pop_back();
        blist.pop_back();
    }
    // print the output
    cout << blist.size() << '\n';
}
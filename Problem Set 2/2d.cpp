/*
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  - https://stackoverflow.com/questions/5131647/why-would-we-call-cin-clear-and-cin-ignore-after-reading-input
  - https://cplusplus.com/reference/string/string/getline/
  - https://linuxhint.com/list-iterator-cpp/
  - https://cplusplus.com/reference/list/list/erase/
  - https://cplusplus.com/reference/list/list/insert/
  - https://www.geeksforgeeks.org/range-based-loop-c/
  I have provide the reasonings to refrence each link over each comment

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I didn't collaborate with anyone for this problem.

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
*/

#include <iostream>
#include <list>
#include <string>
using namespace std;

int main()
{
    int num;
    cin >> num;
    // avoid reading anything after the number, clear the input buffer to prevent reading anything before the next line
    // learned from the link below
    // https://stackoverflow.com/questions/5131647/why-would-we-call-cin-clear-and-cin-ignore-after-reading-input
    cin.ignore();

    //  for each subsequent lines
    for (int i = 0; i < num; i++)
    {
        string str;
        // output string to print the result
        list<char> output;

        // read the whole line using the getline fucntion, return as string. Learned from the link below:
        // https://cplusplus.com/reference/string/string/getline/
        getline(cin, str);

        // List iterator
        // I have learned the concept of list iterators in C++, as well how to some of its related function like begin() and end(). Learned from the link below:
        // https://linuxhint.com/list-iterator-cpp/
        list<char>::iterator iter = output.begin();

        // for (char c : str)
        // for (string::iterator i = str.begin(); i != str.end(); i++)
        for (int i = 0; i < str.length(); i++)
        {
            // When the cursor is NOT at front, perform the backspace operation(delete the previous index's character)
            // Otherwise don't do anything
            if (str[i] == '<')
            {
                if (iter != output.begin())
                {
                    // use erase instead of remove to avoid deleting multiple duplciating elements at once. Learned from the link below:
                    // https://cplusplus.com/reference/list/list/erase/
                    iter = output.erase(iter);
                    iter--;
                }
            }
            // if the character is '[', then shift the iterator to the start of the output list for future insertion/ erase
            else if (str[i] == '[')
            {
                iter = output.begin();
            }
            // if the character is ']', then shift the iterator to the end of the output list for future insertion/ erase
            else if (str[i] == ']')
            {
                iter = output.end();
            }
            // regular case: insert the characters into the output list
            // Use the insert method to insert the elements at the given index iter, learned from the link below:
            // https://cplusplus.com/reference/list/list/insert/
            else
            {
                iter = output.insert(iter, str[i]);
                iter++;
            }
        }
        // Use range based for loop to print the elements in the output list, I have learned the concept of range based for loop in C++ from the link below:
        // https://www.geeksforgeeks.org/range-based-loop-c/
        // for (char x : out)
        // for (std::list<char>::iterator it = out.begin(); it != out.end(); ++it)
        for (auto x : output)
        {
            cout << x;
        }
    }
}
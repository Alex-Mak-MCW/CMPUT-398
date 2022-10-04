#include <iostream>
#include <string>
#include <list>
#include <math.h>
using namespace std;
// Key is to convert binary to decimal

double cul(string str, int j, int len)
{
    int k = j + 1;
    int cetz = 0, cetx = -1;
    long Sumz = 0;
    double Sumx = 0;

    for (; j > 0; j--)
    {
        Sumz += (str[j - 1] - '0') * pow(2, cetz);
        cetz++;
    }
    // cout << cetz << endl;
    for (; k < len; k++)
    {
        Sumx += (str[k] - '0') * pow(2, cetx);
        cetx--;
    }
    // cout << cetx << endl;
    return Sumz + Sumx;
}

int main()
{
    // Read inputs
    int n, d;
    string s;

    cin >> n;
    cin >> d;
    // Use string to read the last line as a whole, access each char in the string
    cin >> s;

    // double x = cul(s, s.find('.'), s.size());

    // exp 1 and 2 used to calculate decimal from binary number
    // exp2 is -1 because to handle the decimal number after the decimal point
    int exp1 = 0, exp2 = -1;
    double x = 0;

    // Binary to decimal part
    // Part before the decimal point, compute the decimal for the whole number
    // find the index that first exist the '.' from the string
    // https://www.techiedelight.com/find-index-of-a-character-in-string-in-cpp/
    for (int j = s.find('.'); j > 0; j--)
    {
        x += (s[j - 1] - '0') * pow(2, exp1);
        exp1++;
    }
    // Part after the decimal point, compute the decinal afterwards
    for (int k = s.find('.') + 1; k < s.size(); k++)
    {
        x += (s[k] - '0') * pow(2, exp2);
        exp2--;
    }

    // cout << x << endl;

    // define the possibilities pa and pb
    double pa = d * 1.0 / 8,
           pb = 1.0 - pa;

    // Implementing the math and concatenate the output string
    for (int i = 0; i < pow(2, n); i++)
    {
        double a = 0, b = 1;
        string output;
        for (int j = 0; j < n; j++)
        {
            double c = a + pa * (b - a);

            // between i and 1*2^j, if both of their operands are 1, then concatenate A to output
            // the interval will be from [a,b) to [a,c), so just update b with c
            if (i & (1 << j))
            {
                output += "A";
                b = c;
            }
            // Otherwise concatenate B to the output
            // the interval will be from [a,b) to [c,b), so just update a with c
            else
            {
                output += "B";
                a = c;
            }
        }
        // if a from the interval is the same as decimal, print the output
        if (a == x)
        {
            cout << output << endl;
            return 0;
        }
    }
}
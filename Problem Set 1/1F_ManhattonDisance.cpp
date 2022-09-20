#include <bits/stdc++.h>

using namespace std;
const long double PI = acos(-1.0);
const double eps = 1e-6;
const int INF = 0x3f3f3f3f;
long double M, N, R;
long double ax, ay, bx, by;

int main()
{
    cin >> M >> N >> R >> ax >> ay >> bx >> by;
    long double r = R / N;

    long double ans1 = r * (fabs(ay - by)) + acos(-1) * r * min(ay, by) * fabs(ax - bx) / M;
    long double ans2 = r * fabs(ay + by);
    printf("%.14LF\n", min(ans1, ans2))
}
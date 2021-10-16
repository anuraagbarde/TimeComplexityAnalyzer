#include <iostream>
#include <string>
using namespace std;
typedef unsigned long long int llu;
int main(int argc, char *argv[])
{
    llu n;
    n = stoi(argv[1]);
    llu sum = 0;
    for (llu i = 0; i < n * n; i++)
        sum += i % 10000;
    // cout << n;

    return 0;
}
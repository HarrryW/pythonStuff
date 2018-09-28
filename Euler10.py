# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def is_prime(candidate):
    for n in range(2, candidate):
        if candidate % n == 0:
            return False
    return True

def main():
    sum = 2
    for n in xrange(3,2000000,2):
        if is_prime(n):
            sum += n
    return sum

print(main())
#This is super slow

#include<bits/stdc++.h>
# #include <iostream>
# using namespace std;
# const int n = 2000000;
# bool ar[n];
# void mul(int a)
# {
#     int i = 2;int p = i*a;
#     while(p < n)
#     {
#         ar[p] = 1;
#         ++i;p = i*a;
#     }
# }
# long long sieve()
# {
#     long long sum = 2;
#     for(int i = 3;i < n;i += 2)
#     {
#         if(ar[i] == 0)
#             sum += i,mul(i);
#     }
#     return sum;
# }
# int main()
# {
#     cout<<sieve();
#     return 0;
# }

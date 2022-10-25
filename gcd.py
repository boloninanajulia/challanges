"""
Task
Given two integers a and b, find their greatest common divisor.

Input Format: The two integers a, b are given in the same line separated by space.
Constraints:  1≤a,b≤2·10**9.
Output Format:  Output GCD(a, b).
"""


# Euclidean algorithm
def gcd(a, b):
    if a == 0 or b == 0:
        return a + b

    if a > b:
        a = a % b
    else:
        b = b % a

    return gcd(a, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))

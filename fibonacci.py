"""
Task
Given an integer n, find the n-th Fibonacci number 𝐹𝑛.

Input Format: The input consists of a single integer n.
Constraints:  0 ≤ n ≤ 45.
Output Format:  Output 𝐹𝑛.
"""


def fibonacci_number(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

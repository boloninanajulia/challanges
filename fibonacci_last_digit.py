"""
Task
Given an integer n, find the last digit of the n-th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).

Input Format: The input consists of a single integer n.
Constraints:  0 ≤ n ≤ 10**7.
Output Format:  Output the last digit of 𝐹𝑛.
"""


def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    fi_digits = [0, 1]

    for _ in range(n - 1):
        previous, current = current, previous + current
        fi_digits.append(current % 10)
        fi_digits_length = len(fi_digits)
        half_fi_digits_length = int(fi_digits_length/2)
        if fi_digits_length % 2 == 0 and fi_digits[:half_fi_digits_length] == fi_digits[half_fi_digits_length:]:
            return fi_digits[n % half_fi_digits_length]

    return fi_digits[-1]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))

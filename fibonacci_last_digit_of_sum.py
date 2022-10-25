"""
Task
Given an integer n, find the last digit of the sum 𝐹0 +𝐹1 +···+𝐹𝑛.

Input Format: The input consists of a single integer n.
Constraints:  0 ≤ n ≤ 10**14.
Output Format:  Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
"""


def fibonacci_last_digit_of_sum(n):
    if n <= 1:
        return n

    digits = [0, 1]

    for _ in range(n - 1):
        digits.append((digits[-2] + digits[-1] + 1) % 10)
        digits_length = len(digits)
        half_digits_length = int(digits_length / 2)
        if digits_length % 2 == 0 and digits[:half_digits_length] == digits[half_digits_length:]:
            return digits[n % digits_length]

    return digits[-1]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit_of_sum(n))

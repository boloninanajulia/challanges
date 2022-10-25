"""
Task. Maximum Pairwise Product Problem
Find the maximum product of two distinct numbers in a sequence of non-negative integers.

Input Format: A sequence of non-negative integers.
Output Format: The maximum value that can be obtained by multiplying two different elements from the sequence.
"""


def max_pairwise_product(numbers):
    max_1 = numbers[0]
    max_2 = numbers[1]
    if max_1 < max_2:
        max_2, max_1 = max_1, max_2

    for n in numbers[2:]:
        if n >= max_1:
            max_1, max_2 = n, max_1
        elif n > max_2:
            max_2 = n

    return max_1*max_2


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))

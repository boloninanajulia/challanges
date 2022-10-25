"""
Task
Given two integers a and b, find their least common multiple.

Input Format: The two integers 𝑎 and 𝑏 are given in the same line separated by space.
Constraints:  1 ≤ a, b ≤ 10**7.
Output Format: Output the least common multiple of a and b.
"""


def simple_numbers__iterator(stop=2):
    yield 2
    remembered = [2]
    for i in range(3, stop+1, 2):
        for j in remembered:
            if i % j == 0:
                return
        yield i


# def multipliers__iterator(n):
#     current = n
#     for simple_number in simple_numbers__iterator(n):
#         while current % simple_number == 0:
#             yield simple_number
#             current /= simple_number


def lcm(a, b):
    multiple_simple_multipliers = 1
    max_number = max(a, b)

    current_a = a
    current_b = b
    for simple_number in simple_numbers__iterator(max_number):
        a_include = current_a % simple_number == 0
        b_include = current_b % simple_number == 0

        while (a_include or b_include) and (current_a != 1 or current_b != 1):
            multiple_simple_multipliers *= simple_number
            if a_include:
                current_a /= simple_number
            if b_include:
                current_b /= simple_number

            a_include = current_a % simple_number == 0
            b_include = current_b % simple_number == 0

    return multiple_simple_multipliers


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))


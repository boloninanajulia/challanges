"""
Task
Compute the last digit of 𝐹02 +𝐹12 +···+𝐹𝑛2.

Input Format: Integer n.
Constraints:  0 ≤ n ≤ 10**14.
Output Format:  The last digit of 𝐹02 + 𝐹12 + · · · + 𝐹𝑛2.
"""


def fibonacci_sum_squares(n):
    if n <= 2:
        return n

    previous = 0
    current = 1

    fi_digits = [0, 1]
    fi_digits_length = 2

    for _ in range(n - 1):
        previous, current = current, previous + current
        fi_digits.append(current % 10)
        fi_digits_length += 1
        half_fi_digits_length = int(fi_digits_length/2)
        if fi_digits_length % 2 == 0 and fi_digits[:half_fi_digits_length] == fi_digits[half_fi_digits_length:]:
            fi_digits = fi_digits[:half_fi_digits_length]
            break

    fi_digits_length = len(fi_digits)
    index = n % fi_digits_length
    prev_index = index-1 if index >= 1 else -1
    return fi_digits[index]*(fi_digits[index]+fi_digits[prev_index]) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))

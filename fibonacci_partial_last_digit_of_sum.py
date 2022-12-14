"""
Task
Given two non-negative integers m and n, where m โค n, find the last digit of the sum ๐น๐ + ๐น๐+1 + ยทยทยท+๐น๐.

Input Format: The input consists of two non-negative integers m and n separated by a space.
Constraints:  0 โค m โค n โค 10**14.
Output Format:  Output the last digit of ๐น๐ + ๐น๐+1 + ยท ยท ยท + ๐น๐.
"""


def fibonacci_partial_last_digit_of_sum(m, n):
    fi_digits = [0, 1]

    if n <= 1:
        return sum(fi_digits[m:n+1])

    for _ in range(n-1):
        fi_digits.append((fi_digits[-2] + fi_digits[-1]) % 10)
        fi_digits_length = len(fi_digits)
        half_fi_digits_length = int(fi_digits_length / 2)
        if fi_digits_length % 2 == 0 and fi_digits[:half_fi_digits_length] == fi_digits[half_fi_digits_length:]:
            fi_digits = fi_digits[:half_fi_digits_length]
            break

    fi_digits_length = len(fi_digits)
    _m = m % fi_digits_length
    _n = n % fi_digits_length
    if _m <= _n:
        return sum(fi_digits[_m:_n+1]) % 10

    return (sum(fi_digits[:_n+1]) + sum(fi_digits[_m:])) % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_last_digit_of_sum(from_, to))

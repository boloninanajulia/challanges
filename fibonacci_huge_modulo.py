"""
Task
Given two integers n and m, output ð¹ð mod m (that is, the remainder of ð¹ð when divided by m).

Input Format: The input consists of two integers n and m given on the same line (separated by a space).
Constraints:  1â¤nâ¤10**14,2â¤mâ¤10**3.
Output Format:  Output ð¹ð mod m.
"""


def fibonacci_huge_modulo(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    modules = [0, 1]
    modules_length = 2

    for _ in range(n - 1):
        previous, current = current, previous + current
        modules.append(current % m)
        modules_length = len(modules)
        half_modules_length = int(modules_length/2)
        if modules_length % 2 == 0 and modules[:half_modules_length] == modules[half_modules_length:]:
            break

    return modules[n % modules_length]


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_modulo(n, m))

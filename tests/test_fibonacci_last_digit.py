from fibonacci_last_digit import fibonacci_last_digit

from .code_quality_score.generate_datasets import random_integer_number__iterator
from .code_quality_score import stress_testing, speed_testing


class TestFibonacciLastDigit:
    @staticmethod
    def fibonacci_last_digit_right(n):
        if n <= 1:
            return n

        previous = 0
        current = 1

        for _ in range(n - 1):
            previous, current = current, previous + current

        return current % 10

    def test_by_stress_testing(self):
        stress_testing(
            fibonacci_last_digit, self.fibonacci_last_digit_right,
            args_iterator=random_integer_number__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 0, 'max_number': 20})

    def test_by_speed_testing(self):
        speed_testing(
            fibonacci_last_digit,
            args_iterator=random_integer_number__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 0, 'max_number': 10**7})

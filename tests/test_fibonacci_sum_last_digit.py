from fibonacci_last_digit_of_sum import fibonacci_last_digit_of_sum

from .code_quality_score.generate_datasets import random_integer_number__iterator
from .code_quality_score import stress_testing, speed_testing


class TestFibonacciSumLastDigit:
    @staticmethod
    def fibonacci_last_digit_of_sum_right(n):
        if n <= 1:
            return n

        previous, current, _sum = 0, 1, 1

        for _ in range(n - 1):
            previous, current = current, previous + current
            _sum += current

        return _sum % 10

    def test_by_stress_testing(self):
        stress_testing(
            fibonacci_last_digit_of_sum, self.fibonacci_last_digit_of_sum_right,
            args_iterator=random_integer_number__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 0, 'max_number': 20})

    def test_by_speed_testing(self):
        speed_testing(
            fibonacci_last_digit_of_sum,
            args_iterator=random_integer_number__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 0, 'max_number': 10**14})

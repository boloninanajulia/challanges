from fibonacci import fibonacci_number

from .code_quality_score.generate_datasets import random_integer_number__iterator
from .code_quality_score import stress_testing, speed_testing


class TestFibonacci:
    def fibonacci_number_right(self, n):
        if n <= 1:
            return n

        return self.fibonacci_number_right(n - 1) + self.fibonacci_number_right(n - 2)

    def test_by_stress_testing(self):
        stress_testing(
            fibonacci_number, self.fibonacci_number_right,
            args_iterator=random_integer_number__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 0, 'max_number': 20})

    def test_by_speed_testing(self):
        speed_testing(
            fibonacci_number,
            args_iterator=random_integer_number__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 0, 'max_number': 45})

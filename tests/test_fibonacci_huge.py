from fibonacci_huge_modulo import fibonacci_huge_modulo

from .code_quality_score.generate_datasets import random_integer_numbers__iterator2
from .code_quality_score import stress_testing, speed_testing


class TestFibonacciHuge:
    @staticmethod
    def fibonacci_huge_modulo_right(n, m):
        if n <= 1:
            return n

        previous = 0
        current = 1

        for _ in range(n - 1):
            previous, current = current, previous + current

        return current % m

    def test_by_stress_testing(self):
        stress_testing(
            fibonacci_huge_modulo, self.fibonacci_huge_modulo_right,
            args_iterator=random_integer_numbers__iterator2,
            args_iterator_kwargs={
                'steps': 100,
                'random_number_limiters': [
                    {'min_number': 1, 'max_number': 10*7},
                    {'min_number': 2, 'max_number': 10*3}
                ]
            }
        )

    def test_by_speed_testing(self):
        speed_testing(
            fibonacci_huge_modulo,
            args_iterator=random_integer_numbers__iterator2,
            args_iterator_kwargs={
                'steps': 100,
                'random_number_limiters': [
                    {'min_number': 1, 'max_number': 10**14},
                    {'min_number': 2, 'max_number': 10**3}
                ]
            }
        )

from gcd import gcd

from .code_quality_score.generate_datasets import random_integer_numbers__iterator
from .code_quality_score import stress_testing, speed_testing


class TestGCD:
    @staticmethod
    def gcd_right(a, b):
        current_gcd = 1
        for d in range(2, min(a, b) + 1):
            if a % d == 0 and b % d == 0:
                if d > current_gcd:
                    current_gcd = d

        return current_gcd

    def test_by_stress_testing(self):
        stress_testing(
            gcd, self.gcd_right,
            args_iterator=random_integer_numbers__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 1, 'max_number': 20})

    def test_by_speed_testing(self):
        speed_testing(
            gcd,
            args_iterator=random_integer_numbers__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 1, 'max_number': 2*10**9})

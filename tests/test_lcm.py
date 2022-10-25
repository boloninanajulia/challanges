from lcm import lcm

from .code_quality_score.generate_datasets import random_integer_numbers__iterator
from .code_quality_score import stress_testing, speed_testing


class TestLCM:
    @staticmethod
    def lcm_right(a, b):
        for l in range(1, a * b + 1):
            if l % a == 0 and l % b == 0:
                return l

        assert False

    def test_by_stress_testing(self):
        stress_testing(
            lcm, self.lcm_right,
            args_iterator=random_integer_numbers__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 1, 'max_number': 20})

    def test_by_speed_testing(self):
        speed_testing(
            lcm,
            args_iterator=random_integer_numbers__iterator,
            args_iterator_kwargs={'steps': 5, 'min_number': 10**6, 'max_number': 10**7})

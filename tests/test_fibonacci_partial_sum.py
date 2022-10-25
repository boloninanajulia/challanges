from fibonacci_partial_last_digit_of_sum import fibonacci_partial_last_digit_of_sum

from .code_quality_score.generate_datasets import get_random_integer_number
from .code_quality_score import stress_testing, speed_testing


class TestFibonacciPartialSum:
    @staticmethod
    def fibonacci_partial_last_digit_of_sum_right(m, n):
        _sum = 0

        current = 0
        _next = 1

        for i in range(n + 1):
            if i >= m:
                _sum += current

            current, _next = _next, current + _next

        return _sum % 10

    @staticmethod
    def random_integer_numbers__iterator(steps, min_number, max_number):
        for _ in range(steps):
            from_ = get_random_integer_number(min_number=min_number, max_number=max_number)
            to = get_random_integer_number(min_number=from_, max_number=max_number)
            yield (from_, to)

    def test_by_stress_testing(self):
        stress_testing(
            fibonacci_partial_last_digit_of_sum, self.fibonacci_partial_last_digit_of_sum_right,
            args_iterator=self.random_integer_numbers__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 0, 'max_number': 2000})

    def test_by_speed_testing(self):
        speed_testing(
            fibonacci_partial_last_digit_of_sum,
            args_iterator=self.random_integer_numbers__iterator,
            args_iterator_kwargs={'steps': 100, 'min_number': 0, 'max_number': 10**14})

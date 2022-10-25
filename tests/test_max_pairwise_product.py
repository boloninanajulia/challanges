import json

from .code_quality_score import stress_testing, speed_testing

from max_pairwise_product import max_pairwise_product


class TestMaxPairwiseProduct:
    @staticmethod
    def max_pairwise_product_right(numbers):
        n = len(numbers)
        max_product = 0
        for first in range(n):
            for second in range(first + 1, n):
                max_product = max(max_product,
                                  numbers[first] * numbers[second])

        return max_product

    @staticmethod
    def read_dataset(file):
        for input_numbers in file.readlines():
            yield (json.loads(input_numbers), )

    def test_stress_max_pairwise_product(self):
        with open("./tests/code_quality_score/dataset_list.txt", "r") as file:
            stress_testing(
                max_pairwise_product, self.max_pairwise_product_right,
                args_iterator=self.read_dataset, args_iterator_kwargs={'file': file})

    # def test_speed_max_pairwise_product(self):
    #     with open("./tests/code_quality_score/big_dataset_list.txt", "r") as file:
    #         speed_testing(
    #             max_pairwise_product,
    #             args_iterator=self.read_dataset, args_iterator_kwargs={'file': file})

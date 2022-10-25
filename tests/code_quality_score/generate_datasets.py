import random


max_integer_number = 2*10**5


def random_integer_numbers__iterator(steps, min_number, max_number, number_count=2) -> tuple:
    for i in range(steps):
        numbers = []
        for _ in range(number_count):
            numbers.append(get_random_integer_number(min_number=min_number, max_number=max_number))

        yield tuple(numbers)


def random_integer_numbers__iterator2(steps, random_number_limiters) -> tuple:
    for i in range(steps):
        numbers = []
        for limit in random_number_limiters:
            numbers.append(get_random_integer_number(min_number=limit['min_number'], max_number=limit['max_number']))

        yield tuple(numbers)


def random_integer_number__iterator(steps, min_number, max_number) -> tuple:
    for i in range(steps):
        yield (get_random_integer_number(min_number=min_number, max_number=max_number),)


def get_random_integer_number(min_number=0, max_number=max_integer_number):
    return random.randint(min_number, max_number)


def create_integer_dataset_list(filename, lines=20, steps=100, min_number=1, max_number=max_integer_number):
    with open(filename, "a") as f:
        for i in range(0, lines):
            integer_list = []
            for random_number in random_integer_number__iterator(
                    steps=steps,
                    min_number=min_number,
                    max_number=max_number
            ):
                integer_list.append(random_number)
            print(f'write {i} {integer_list}')
            f.write(f"{integer_list}\n")


if __name__ == '__main__':
    create_integer_dataset_list("dataset_list.txt", lines=20, steps=100)
    create_integer_dataset_list("big_dataset_list.txt", lines=20, steps=max_integer_number)

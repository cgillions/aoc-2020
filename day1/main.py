import itertools
import requests
import math


def get_cookie() -> str:
    with open('.aoc-cookie') as file:
        return file.read()


def get_input(url) -> list:
    text = requests.get(url, cookies={'session': get_cookie()}).text
    return [int(i) for i in text.strip().split('\n')]


def get_group_that_sum_to(input: list, group_size: int, target: int) -> tuple:
    for entry in itertools.combinations(input, group_size):
        if sum(entry) == target:
            yield entry


def main():
    target = 2020
    input = get_input('https://adventofcode.com/2020/day/1/input')

    # Find the answers for part 1 & part 2.
    for size, label in {2: 'pairs', 3: 'trios'}.items():
        entry = next(get_group_that_sum_to(input, size, target))
        product = str(math.prod(entry))
        print(f'The product of the input {label} that sums to {target} are:')
        print(product)
        print()


if __name__ == '__main__':
    main()

from functools import reduce
from itertools import product
import operator
from typing import Iterable, TextIO
from sys import stdin

YEAR = 2020

def load_data(file: TextIO):
    return [int(line) for line in file.readlines() if line != ""]

def solve(numbers: Iterable[int], entries: int = 2):
    subsets = product(data, repeat=entries)
    for subset in subsets:
        if sum(subset) == YEAR:
            return reduce(operator.mul, subset, 1)

if __name__ == "__main__":
    data = load_data(stdin)
    print(f"task 1: {solve(data)}")
    print(f"task 2: {solve(data, 3)}")

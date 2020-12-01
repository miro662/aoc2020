from functools import partial, reduce
from itertools import product
from operator import mul
import time
from typing import Any, Callable, Iterable, List, TextIO
from sys import stdin

YEAR = 2020

def load_data(file: TextIO):
    return [int(line) for line in file.readlines() if line != ""]


def solve(numbers: Iterable[int], entries: int = 2):
    subsets = product(numbers, repeat=entries)
    for subset in subsets:
        if sum(subset) == YEAR:
            return reduce(mul, subset, 1)


def solve_nlogn_2(numbers: List[int], already_sorted: bool = False, desired_sum: int = YEAR):
    sorted_numbers = numbers if already_sorted else sorted(numbers) 
    l = 0
    r = len(sorted_numbers) - 1
    while l != r:
        s = sorted_numbers[l] + sorted_numbers[r] 
        if s == desired_sum:
            return sorted_numbers[l] * sorted_numbers[r]
        elif s > desired_sum:
            r -= 1
        elif s < desired_sum:
            l += 1


def solve_n2_3(numbers: Iterable[int]):
    sorted_numbers = sorted(numbers)
    for number in sorted_numbers:
        without_number = [n for n in sorted_numbers if n != number]
        result = solve_nlogn_2(without_number, already_sorted=True, desired_sum=YEAR - number)
        if result:
            return result * number


def benchmark(message: str, function: Callable[[], Any]):
    start_time = time.time_ns()
    result = function()
    end_time = time.time_ns()
    duration = end_time - start_time
    print(f"{message}: {result}; duration: {duration} ns")


if __name__ == "__main__":
    data = load_data(stdin)
    benchmark("task 1, O(n^2)", partial(solve, data))
    benchmark("task 2, O(n^3)", partial(solve, data, entries=3))
    benchmark("task 1, O(n log n)", partial(solve_nlogn_2, data))
    benchmark("task 2, O(n^2)", partial(solve_n2_3, data))

import time
import numpy as np

SIZE = 10_000_000

def python_sum():
    numbers = list(range(SIZE))

    start = time.perf_counter()

    total = 0

    for number in numbers:
        total += number

    end = time.perf_counter()

    return total, end - start

def numpy_sum():
    numbers = np.arange(SIZE)

    start = time.perf_counter()

    total = np.sum(numbers)

    end = time.perf_counter()

    return total, end - start

def main():
    python_total, python_time = python_sum()
    numpy_total, numpy_time = numpy_sum()

    print(f"Python Total : {python_total}")
    print(f"Python Time  : {python_time:.4f} seconds")

    print()

    print(f"NumPy Total  : {numpy_total}")
    print(f"NumPy Time   : {numpy_time:.4f} seconds")
if __name__ == "__main__":
    main()

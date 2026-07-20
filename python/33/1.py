"""
1. Среднее время выполнения

Создайте декоратор measure_time, который измеряет и выводит среднее время
выполнения функции за 5 вызовов. Функция может быть любой: например,
сортировка списка, чтение из файла или расчёты.

Пример применения:
    @measure_time
    def compute():
        total = 0
        for i in range(10_000_000):
            total += i
        return total

Пример вывода:
    Среднее время выполнения для 5 вызовов: 0.21 секунд
    Результат: 49999995000000
"""

from functools import wraps
from time import perf_counter


def measure_time(function):
    """Измеряет среднее время выполнения функции за пять вызовов."""

    @wraps(function)
    def wrapper(*args, **kwargs):
        repeats = 5
        total_time = 0
        result = None

        for _ in range(repeats):
            start_time = perf_counter()
            result = function(*args, **kwargs)
            total_time += perf_counter() - start_time

        average_time = total_time / repeats
        print(
            f"Среднее время выполнения для {repeats} вызовов: "
            f"{average_time:.2f} секунд"
        )
        print(f"Результат: {result}")
        return result

    return wrapper


@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


if __name__ == "__main__":
    compute()

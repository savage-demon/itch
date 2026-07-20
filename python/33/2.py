"""
2. Среднее время выполнения с количеством вызовов

Доработайте декоратор measure_time, чтобы он принимал параметр repeats —
количество вызовов функции. Декоратор должен выполнять функцию указанное
число раз и выводить среднее время выполнения.

Пример применения:
    @measure_time(10)
    def compute():
        total = 0
        for i in range(10_000_000):
            total += i
        return total

Пример вывода:
    Среднее время выполнения для 10 вызовов: 0.21 секунд
    Результат: 49999995000000
"""

from functools import wraps
from time import perf_counter


def measure_time(repeats):
    """Создаёт декоратор для измерения среднего времени вызовов функции."""
    if repeats <= 0:
        raise ValueError("Количество вызовов должно быть больше нуля")

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
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

    return decorator


@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


if __name__ == "__main__":
    compute()

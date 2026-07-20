"""
Рамка вокруг вывода

Создайте декоратор frame, который оборачивает результат функции рамкой из
50 символов -, выводя по строке до и после вызова функции.

Пример декорируемой функции:
    def say_hello():
        print("Привет, игрок!")

Пример вывода:
    --------------------------------------------------
    Привет, игрок!
    --------------------------------------------------
"""


from functools import wraps


def frame(function):
    """Выводит рамку из 50 дефисов до и после вызова функции."""

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("-" * 50)
        result = function(*args, **kwargs)
        print("-" * 50)
        return result

    return wrapper


@frame
def say_hello():
    print("Привет, игрок!")


if __name__ == "__main__":
    say_hello()

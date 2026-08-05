# Фигуры и площади
#
# Создайте абстрактный класс Shape.
#
# В классе должен быть метод area(), который возвращает площадь фигуры.
#
# Реализуйте два класса:
#
# Circle, который принимает радиус.
#
# Rectangle, который принимает ширину и высоту.
#
#
# # Пример использования
#
# shapes = [Circle(3), Rectangle(4, 5)]
#
# for shape in shapes:
#
#     print(f"Area: {shape.area():.2f}")
#
#
# Проверка размеров фигур
#
# Доработайте фигуры:
#
# Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
#
# Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение InvalidSizeError.

from abc import ABC, abstractmethod
from math import pi


class InvalidSizeError(ValueError):
    """Размер фигуры должен быть положительным."""


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Возвращает площадь фигуры."""


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("Радиус должен быть положительным")
        self.radius = radius

    def area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError(
                "Ширина и высота должны быть положительными"
            )
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    shapes = [Circle(3), Rectangle(4, 5)]

    for shape in shapes:
        print(f"Area: {shape.area():.2f}")

"""
1. Класс Rectangle

Создайте класс Rectangle, который описывает прямоугольник.

- У каждого объекта должны быть два поля: width и height.
- Добавьте метод get_area(), который возвращает площадь прямоугольника.
- Создайте объект прямоугольника с произвольными значениями.
- Выведите его площадь.
- Измените ширину и высоту.
- Выведите новую площадь.

Пример вывода:
    Площадь: 20
    Новая площадь: 35
"""


class Rectangle:
    """Описывает прямоугольник с заданными шириной и высотой."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height



rectangle = Rectangle(4, 5)
print(f"Площадь: {rectangle.get_area()}")

rectangle.width = 7
rectangle.height = 5
print(f"Новая площадь: {rectangle.get_area()}")

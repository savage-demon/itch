""" 01 Класс Person

Создайте класс Person, представляющий человека.
- Каждый человек должен иметь имя.
- Добавьте метод introduce(), который выводит приветствие с именем.

Пример вывода:
Hello, my name is Alice.
"""


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


if __name__ == "__main__":
    person1 = Person("Alice")
    person1.introduce()

# Hello, my name is Alice.

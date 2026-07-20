"""
Расширяемый логгер событий

Создайте функцию, которая возвращает вложенный логгер событий. Каждый вызов
логгера должен сохранять событие с текущим временем (если оно передано) и
возвращать весь список событий.

Пример вызова:
    log("Загрузка данных")
    log("Обработка завершена")
    log("Сохранение файла")

    for event in log():
        print(event)

Пример вывода:
    Загрузка данных: 2025-03-24 14:06:29
    Обработка завершена: 2025-03-24 14:06:29
    Сохранение файла: 2025-03-24 14:06:29
"""


from datetime import datetime


def make_logger():
    """Возвращает логгер, сохраняющий события и время их добавления."""
    events = []

    def log(message=None):
        if message is not None:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            events.append(f"{message}: {current_time}")

        return events.copy()

    return log


if __name__ == "__main__":
    log = make_logger()

    log("Загрузка данных")
    log("Обработка завершена")
    log("Сохранение файла")

    for event in log():
        print(event)

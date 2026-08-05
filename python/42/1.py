# Создание базы
#
# Напишите программу, которая:
#
# создаёт базу данных notes_app_<your_group>_<your_full_name>
#
# выбирает эту базу через USE notes_app
#
# выводит сообщение о результате
#
#
#
# Добавление заметок
#
# Продолжите предыдущую программу:
#
# создайте таблицу notes с полями: id, title, content
#
# вставьте одну заметку в таблицу
#
# выполните commit() после вставки
#
# выведите все заметки используя DictCursor

import os

DATABASE_NAME = "notes_app_ich1_dmitriy_hellwig"

def connect_to_mysql(database=None):
    import pymysql

    return pymysql.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=database,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def main():
    database_name = DATABASE_NAME

    connection = connect_to_mysql()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS `{database_name}` "
                "CHARACTER SET utf8mb4"
            )
            cursor.execute(f"USE `{database_name}`")
            print(f"База данных {database_name} создана и выбрана.")

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS notes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    content TEXT NOT NULL
                )
                """
            )
            cursor.execute(
                "INSERT INTO notes (title, content) VALUES (%s, %s)",
                ("Первая заметка", "Текст первой заметки"),
            )
            connection.commit()

            cursor.execute("SELECT id, title, content FROM notes")
            notes = cursor.fetchall()

        for note in notes:
            print(note)
    finally:
        connection.close()


if __name__ == "__main__":
    main()

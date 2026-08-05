# Список всех стран
#
# Используя базу данных world, выведи названия всех стран из таблицы country. Каждое название должно отображаться с новой строки и иметь номер.
#
# Города выбранной страны
#
# Добавьте к предыдущей программе возможность выбора страны. Пользователь введёт название или номер из выведенного списка. Далее выведите все города этой страны и их численность населения, также с нумерацией.

import os
from pathlib import Path
from urllib.parse import unquote, urlsplit

from dotenv import load_dotenv


load_dotenv(Path(__file__).with_name(".env"))


def connect_to_world():
    """Создаёт подключение к учебной базе world."""
    import pymysql

    database_url = os.getenv("DB_URL")
    if not database_url:
        raise RuntimeError("Переменная DB_URL не задана")

    connection_data = urlsplit(database_url)

    return pymysql.connect(
        host=connection_data.hostname,
        port=connection_data.port or 3306,
        user=unquote(connection_data.username or ""),
        password=unquote(connection_data.password or ""),
        database=os.getenv("MYSQL_DATABASE", "world"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def get_countries(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT Code, Name FROM country ORDER BY Name")
        return cursor.fetchall()


def select_country(countries, choice):
    choice = choice.strip()

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(countries):
            return countries[index]
        return None

    return next(
        (
            country
            for country in countries
            if country["Name"].casefold() == choice.casefold()
        ),
        None,
    )


def get_cities(connection, country_code):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT Name, Population
            FROM city
            WHERE CountryCode = %s
            ORDER BY Name
            """,
            (country_code,),
        )
        return cursor.fetchall()


def main():
    with connect_to_world() as connection:
        countries = get_countries(connection)
        for number, country in enumerate(countries, start=1):
            print(f"{number}. {country['Name']}")

        choice = input("Введите название или номер страны: ")
        country = select_country(countries, choice)
        if country is None:
            print("Страна не найдена.")
            return

        cities = get_cities(connection, country["Code"])
        if not cities:
            print("Для выбранной страны города не найдены.")
            return

        for number, city in enumerate(cities, start=1):
            print(f"{number}. {city['Name']} — {city['Population']}")


if __name__ == "__main__":
    main()

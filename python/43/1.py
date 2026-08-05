# Добавление товаров
#
# Создайте программу, которая подключается к MongoDB и:
#
# выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
#
# очищает коллекцию перед началом
#
# добавляет 3 товара с полями: name, price, stock
#
# выводит сообщение о количестве добавленных товаров
#
#
# Увеличение цен
#
# Продолжите предыдущую задачу. Теперь программа должна:
#
# увеличить цену всех товаров на 20%
#
# вывести количество обновлённых записей
#
# затем вывести список всех товаров с новыми ценами

import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv(Path(__file__).with_name(".env"))


DATABASE_NAME = "ich_edit"
COLLECTION_NAME = "products_ich1_dmitriy_hellwig"


def main():
    from pymongo import MongoClient

    mongo_uri = os.getenv("MONGODB_URI")
    if not mongo_uri:
        raise RuntimeError(
            "Задайте строку подключения в переменной MONGODB_URI"
        )

    with MongoClient(mongo_uri) as client:
        products = client[DATABASE_NAME][COLLECTION_NAME]
        products.delete_many({})

        result = products.insert_many(
            [
                {"name": "Laptop", "price": 1000, "stock": 5},
                {"name": "Mouse", "price": 25, "stock": 30},
                {"name": "Keyboard", "price": 50, "stock": 15},
            ]
        )

        print(f"Добавлено товаров: {len(result.inserted_ids)}")

        update_result = products.update_many(
            {},
            [{"$set": {"price": {"$multiply": ["$price", 1.2]}}}],
        )

        print(f"Обновлено товаров: {update_result.modified_count}")

        for product in products.find(
            {}, {"_id": 0, "name": 1, "price": 1, "stock": 1}
        ):
            print(product)


if __name__ == "__main__":
    main()

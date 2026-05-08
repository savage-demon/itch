# Обновление цен товаров
#
# Дан список товаров с ценами. Программа должна применить скидку
# к каждому товару и добавить в список элемент с новой ценой. 
# В конце вывести таблицу с новой ценой.
#
# Данные:
#
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
#
#
# Пример вывода:
#
# Введите скидку (в процентах): 17
#
# Товар          Старая цена    Новая цена
#
# Laptop            1200.00$       996.00$
#
# Mouse                25.00$         20.75$
#
# Keyboard           75.00$         62.25$
#
# Monitor            200.00$       166.00$
#

NAME, PRICE = 10, 15

line = "-" * (NAME + PRICE * 2)
row_template = f"{{:<{NAME}}}{{:>{PRICE}.2f}}{{:>{PRICE}.2f}}"
header_template = f"{line}\n{{:<{NAME}}}{{:>{PRICE}}}{{:>{PRICE}}}\n{line}"

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

percent = 17

print(header_template.format("Товар", "Старая цена", "Новая цена"))

for product, price in products:
    nprice = price * (1 - percent / 100)

    print(row_template.format(product, price, nprice))

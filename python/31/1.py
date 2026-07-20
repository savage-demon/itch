# Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.
import re


text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."

dates = re.finditer(r"\b\d{2}([./-])\d{2}\1\d{4}\b", text)

for date in dates:
    print(date.group())

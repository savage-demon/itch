# Разделить строку на отдельные теги по запятым, точкам с запятой,
# слешам и пробелам, удалив пустые значения.
import re


tag_input = "python, data-science / machine-learning; AI neural-networks"

tags = [tag for tag in re.split(r"[,;/\s]+", tag_input.strip()) if tag]

print(tags)

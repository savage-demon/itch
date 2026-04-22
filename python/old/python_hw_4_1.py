light_on = bool(int(input("Свет включён? (1 для True, 0 для False): ")))
window_open = bool(int(input("Окно открыто? (1 для True, 0 для False): ")))

both_conditions = light_on and window_open
at_least_one = light_on or window_open

print(f"Оба условия выполнены? {both_conditions}")
print(f"Хотя бы одно условие выполнено? {at_least_one}")

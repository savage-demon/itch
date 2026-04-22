base_price = 30
limit_mb = 500
price_per_extra_mb = 0.2

used_mb = float(input("Введите использованные мегабайты: "))

extra_mb = max(0, used_mb - limit_mb)
extra_cost = extra_mb * price_per_extra_mb

total_cost = base_price + extra_cost

print(f"Общая стоимость: {total_cost}")

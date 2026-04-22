-- 01 Подсчитайте основные статистики - среднее, сумму, минимум, максимум столбца unit_cost.
SELECT
	avg(unit_cost) uc_avg,
	sum(unit_cost) uc_sum,
	min(unit_cost) uc_min
FROM
	purchase_order_details;

-- 02 Подсчитайте количество уникальных заказов purchase_order_id.
SELECT
	count(DISTINCT purchase_order_id) poi_count
FROM
	purchase_order_details;

/* 03 Подсчитайте количество продуктов product_id в каждом заказе purchase_order_id.
   Отсортируйте полученные данные по убыванию количества. */
SELECT
	purchase_order_id,
	count(product_id) p_count
FROM
	purchase_order_details
GROUP BY
	purchase_order_id
ORDER BY
	p_count DESC
;

/* 04 Подсчитайте заказы по дате доставки date_received.
   Считаем только те продукты, количество quantity которых больше 30. */
SELECT
	date_received,
	count(*) orders_count
FROM
	purchase_order_details
WHERE
	quantity > 30
GROUP BY
	date_received;

/* 05 Подсчитайте суммарную стоимость заказов в каждую из дат.
   Стоимость заказа - произведение quantity на unit_cost. */
SELECT
	date_received,
	sum(quantity * unit_cost) orders_price_total
FROM
	purchase_order_details
GROUP BY
	date_received
;


/* 06 Сгруппируйте товары по unit_cost и вычислите среднее и максимальное
   значение quantity только для товаров, где purchase_order_id не больше 100. */
SELECT
	unit_cost,
	avg(quantity) q_avg,
	max(quantity) q_max
FROM
	purchase_order_details
WHERE
	purchase_order_id < 100
GROUP BY
	unit_cost
;

/* 07 Выберите только строки, где есть значения в столбце inventory_id.
Создайте столбец category
   - если unit_cost > 20 то 'Expensive'
   - в остальных случаях  - 'others'.
Посчитайте количество продуктов в каждой категории. */
SELECT
	IF(unit_cost > 20, 'Expensive', 'others') category,
	count(*) cnt
FROM
	purchase_order_details
WHERE
	inventory_id IS NOT NULL
GROUP BY
	category
;

-- 1. Из таблицы order_details вывести все строки там, где purchase_order_id не указано. При этом дополнительно создать столбец total_price как произведение quantity * unit_price
SELECT
	*,
	quantity * unit_price AS total_price
FROM
	order_details
WHERE
	purchase_order_id IS NULL
; 

-- 2. Вывести один столбец из таблицы employees содержащий имя и фамилию написанные через пробел Вывести 3 строки начиная со второй
SELECT
	CONCAT(first_name, ' ', last_name)
FROM
	employees
LIMIT 3 
OFFSET 2
;

-- 3. На основе таблицы orders вывести один столбец - с годом и месяцем из order_date в формате 'год-месяц'
SELECT
	LEFT(order_date, 7)
FROM
	orders
;

-- 4. Выведите уникальные имена компаний из таблицы customers. Отсортируйте их по убыванию
SELECT
	DISTINCT company
FROM
	customers
ORDER BY
	company DESC
;

-- 5. Выведите столбцы id, order_id из таблицы order_details, а также 
-- вычисляемый столбец category в зависимости от значений unit_price. 
-- Если unit_price > 10 то значение столбца  category 'Expensive' 
-- В противном случае — 'Cheap' 
-- Написать запрос двумя способами -  с применением операторов IF и CASE

SELECT
	id,
	order_id,
	unit_price,
	IF(unit_price > 10, 'Expensive', 'Cheap') category_if,
	CASE
		WHEN unit_price > 10 THEN 'Expensive'
		ELSE 'Cheap'
	END category_case
FROM
	order_details;



















-- 1. Выведите текущую дату и время:

SELECT now();

-- 2. Выведите день недели, когда был сделан каждый заказ из таблицы orders:
SELECT dayname(order_date) FROM northwind.orders

-- 3. Добавьте 30 дней к дате каждого заказа в таблице orders и выведите результат:

SELECT date_add(order_date, INTERVAL 30 DAY) FROM northwind.orders

-- 4. Выведите количество дней между датой заказа и датой доставки для каждого заказа из таблицы orders:

SELECT
	datediff(shipped_date, order_date)
FROM
	orders;


-- 5. Найдите все заказы, сделанные в пятницу из таблицы orders:

SELECT *
FROM orders
WHERE dayname(order_date) = 'friday';

-- 6. Выведите дату, которая будет через 100 дней от текущей:

SELECT date_add(curdate(), INTERVAL 100 DAY);


-- 7. Выведите заказы, сделанные в выходные дни (суббота и воскресенье) из таблицы orders:

SELECT *
FROM orders
WHERE dayname(order_date) IN ('saturday', 'sunday'); 


-- 8. Найдите количество дней до конца текущего года:

SELECT datediff('2027-01-01', now())

-- 9. Выведите дату, которая была 15 дней назад от текущей даты:

SELECT date_sub(curdate(), INTERVAL 15 DAY);

-- 10. Примените явное преобразование и выведите столбец id из таблицы customers в виде строки:

SELECT cast(id AS char) FROM customers;

































-- 1   Вывести названия продуктов таблица products, включая количество заказанных единиц quantity для каждого продукта таблица order_details.
-- Решить задачу с помощью cte и подзапроса

SELECT
    (
        SELECT
            product_name
        FROM
            products
        WHERE
            id = product_id
    ) p_name,
    sum(quantity) q_sum
FROM
    order_details
GROUP BY
    product_id;



WITH o AS (
    SELECT
        product_id,
        sum(quantity) q_sum
    FROM
        order_details
    GROUP BY
        product_id
)
SELECT
    p.product_name,
    q_sum
FROM
    products p
JOIN o ON
    p.id = o.product_id;


-- 2  Найти все заказы таблица orders, сделанные после даты самого первого заказа клиента Lee таблица customers.

SELECT
    *
FROM
    orders
WHERE
    order_date > (
        SELECT
            MIN(o.order_date)
        FROM
            orders o
        JOIN customers c ON
            o.customer_id = c.id
        WHERE
            c.last_name = 'Lee'
    );


-- 3 Найти все продукты таблицы  products c максимальным target_level

SELECT
    *
FROM
    products
WHERE
    target_level = (
        SELECT
            max(target_level)
        FROM
            products
    );

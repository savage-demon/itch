-- 2 Создайте таблицу, которая отражает погоду в Вашем городе за последние 5 дней и включает следующее столбцы
-- 
-- Id - первичный ключ, заполняется автоматически
-- 
-- Дата - не может быть пропуском
-- 
-- Дневная температура - целое число, принимает значения от -30 до 30
-- 
-- Ночная температура - целое число, принимает значения от -30 до 30
-- 
-- Скорость ветра - подумайте какой тип данных и ограничения необходимы для этого столбца
-- 
-- 3 Заполните таблицу 5 строками - за последние 5 дней 
-- 
-- 4 Увеличьте значения ночной температуры на градус если скорость ветра не превышала 3 м/с
-- 
-- 5 На основе полученной таблицы создайте представление в своей базе данных - включите все строки Вашей таблицы и дополнительно рассчитанные столбцы
-- 
-- Средняя суточная температура - среднее арифметическое между ночной и дневной температурами
-- 
-- Столбец на основе скорости ветра - если скорость ветра не превышала 2 м/с то значение ‘штиль’, от 2 включительно до 5 - ‘умеренный ветер’, в остальных случаях - ‘сильный ветер’


CREATE TABLE weather_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    measure_date DATE NOT NULL,
    day_temperature TINYINT CHECK (day_temperature BETWEEN -30 AND 30),
    night_temperature TINYINT CHECK (night_temperature BETWEEN -30 AND 30),
    wind_speed_mps DECIMAL(4,1)
);


INSERT INTO weather_logs 
	(measure_date, day_temperature, night_temperature, wind_speed_mps) 
VALUES 
	("2026-04-09", 10, 1, 12.3),
	("2026-04-10", 12, 2, 2.5),
	("2026-04-11", 15, 5, 1.9),
	("2026-04-12", 12, 0, 0.5),
	("2026-04-13", 18, 2, 1.7);


UPDATE
	weather_logs
SET
	night_temperature = night_temperature + 1
WHERE
	wind_speed_mps <= 3;


CREATE VIEW view_weather_logs AS 
SELECT
	id,
	measure_date,
	day_temperature,
	night_temperature,
	wind_speed_mps,
	(day_temperature + night_temperature) / 2 mid_temperature,
	CASE
		WHEN wind_speed_mps <= 2 THEN 'штиль'
		WHEN wind_speed_mps <= 5 THEN 'умеренный ветер'
		ELSE 'сильный ветер'
	END wind_speed_human
FROM
	weather_logs;


-- два метра в секунду не превышает двух метров в секунду, значит штиль, по этому умеренный ветер уже не может быть от двух включительно

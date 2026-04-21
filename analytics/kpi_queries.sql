SELECT id_machine,
       DATE(timestamp) as day,
       SUM(units_produced) as total_production
FROM machine_events
GROUP BY id_machine, DATE(timestamp);

SELECT id_machine,
       DATE(timestamp) as day,
       SUM(units_nok)::float / SUM(units_produced) as scrap_rate
FROM machine_events
GROUP BY id_machine, DATE(timestamp);

SELECT id_machine,
       DATE(timestamp) as day,
       AVG(downtime) as downtime_rate
FROM machine_events
GROUP BY id_machine, DATE(timestamp);

SELECT shift,
       SUM(units_ok) as good_production,
       SUM(units_nok) as scrap
FROM machine_events
GROUP BY shift;
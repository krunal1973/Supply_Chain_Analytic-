SELECT
    `Order Status`,
    COUNT(DISTINCT `Order Id`) AS total_orders
FROM supply_chain
GROUP BY `Order Status`
ORDER BY total_orders DESC;

SELECT
    `Order Status`,
    ROUND(SUM(Sales),2) AS revenue
FROM supply_chain
GROUP BY `Order Status`
ORDER BY revenue DESC;

SELECT
    YEAR(`order date (DateOrders)`) AS year,
    MONTH(`order date (DateOrders)`) AS month,
    COUNT(DISTINCT `Order Id`) AS orders
FROM supply_chain
GROUP BY year, month
ORDER BY year, month;

SELECT
    YEAR(`order date (DateOrders)`) AS year,
    COUNT(DISTINCT `Order Id`) AS orders
FROM supply_chain
GROUP BY year
ORDER BY year;

SELECT
    ROUND(
        SUM(Sales) /
        COUNT(DISTINCT `Order Id`),
        2
    ) AS avg_order_value
FROM supply_chain;

SELECT
    `Order Id`,
    ROUND(SUM(Sales),2) AS order_value
FROM supply_chain
GROUP BY `Order Id`
ORDER BY order_value DESC
LIMIT 10;

SELECT
    `Order Id`,
    ROUND(SUM(Sales),2) AS order_value
FROM supply_chain
GROUP BY `Order Id`
ORDER BY order_value ASC
LIMIT 10;

SELECT
    `Order Status`,
    COUNT(*) AS orders,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM supply_chain),
        2
    ) AS pct
FROM supply_chain
GROUP BY `Order Status`;
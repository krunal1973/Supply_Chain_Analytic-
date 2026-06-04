SELECT
    YEAR(`order date (DateOrders)`) year,
    MONTH(`order date (DateOrders)`) month,
    ROUND(SUM(Sales),2) revenue
FROM supply_chain
GROUP BY year,month
ORDER BY year,month;

SELECT
    YEAR(`order date (DateOrders)`) year,
    MONTH(`order date (DateOrders)`) month,
    ROUND(SUM(`Order Profit Per Order`),2) profit
FROM supply_chain
GROUP BY year,month
ORDER BY year,month;

SELECT
    YEAR(`order date (DateOrders)`) year,
    QUARTER(`order date (DateOrders)`) quarter_no,
    ROUND(SUM(Sales),2) revenue
FROM supply_chain
GROUP BY year,quarter_no
ORDER BY year,quarter_no;

SELECT
    YEAR(`order date (DateOrders)`) year,
    QUARTER(`order date (DateOrders)`) quarter_no,
    ROUND(SUM(`Order Profit Per Order`),2) profit
FROM supply_chain
GROUP BY year,quarter_no
ORDER BY year,quarter_no;

SELECT
    YEAR(`order date (DateOrders)`) year,
    MONTH(`order date (DateOrders)`) month,
    ROUND(SUM(Sales),2) revenue
FROM supply_chain
GROUP BY year,month
ORDER BY revenue DESC; 
SELECT
    Market,
    ROUND(SUM(`Order Profit Per Order`),2) profit
FROM supply_chain
GROUP BY Market
ORDER BY profit DESC;

SELECT
    `Category Name`,
    ROUND(SUM(`Order Profit Per Order`),2) profit
FROM supply_chain
GROUP BY `Category Name`
ORDER BY profit DESC;

SELECT
    `Category Name`,
    ROUND(
        SUM(`Order Profit Per Order`) * 100 /
        SUM(Sales),
        2
    ) margin_pct
FROM supply_chain
GROUP BY `Category Name`
ORDER BY margin_pct DESC;

SELECT
    `Product Name`,
    ROUND(SUM(`Order Profit Per Order`),2) profit
FROM supply_chain
GROUP BY `Product Name`
ORDER BY profit DESC
LIMIT 20;

SELECT
    `Product Name`,
    ROUND(SUM(`Order Profit Per Order`),2) profit
FROM supply_chain
GROUP BY `Product Name`
ORDER BY profit ASC
LIMIT 20;
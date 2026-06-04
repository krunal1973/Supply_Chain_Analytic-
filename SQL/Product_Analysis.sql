select `Product Name`,round(sum(Sales),2) as revenue
from supply_chain group by `Product Name` 
order by revenue desc limit 10 ;

SELECT
    `Product Name`,
    ROUND(SUM(`Order Profit Per Order`), 2) AS profit
FROM supply_chain
GROUP BY `Product Name`
ORDER BY profit DESC
LIMIT 10; 

select `Product Name`,sum(`Order Item Quantity`) 
as quantity_sold from supply_chain 
group by `Product Name` order by quantity_sold desc 
limit 10;

select `Product Name`,round(sum(Sales),2) as revenue,
round((sum(Sales)*100.0)/(select sum(Sales) from supply_chain),
2) as revenue_pct from supply_chain 
group by `Product Name` order by revenue desc limit 10;

SELECT
    `Category Name`,
    COUNT(DISTINCT `Product Name`) AS total_products,
    ROUND(SUM(Sales),2) AS revenue,
    ROUND(SUM(`Order Profit Per Order`),2) AS profit
FROM supply_chain
GROUP BY `Category Name`
ORDER BY revenue DESC;

SELECT
    `Category Name`,
    ROUND(SUM(Sales),2) AS revenue,
    ROUND(
        SUM(Sales) * 100.0 /
        (SELECT SUM(Sales) FROM supply_chain),
        2
    ) AS revenue_pct
FROM supply_chain
GROUP BY `Category Name`
ORDER BY revenue DESC
LIMIT 10;

SELECT
    `Category Name`,
    ROUND(SUM(`Order Profit Per Order`),2) AS profit,
    ROUND(
        SUM(`Order Profit Per Order`) * 100.0 /
        (SELECT SUM(`Order Profit Per Order`) FROM supply_chain),
        2
    ) AS profit_pct
FROM supply_chain
GROUP BY `Category Name`
ORDER BY profit DESC
LIMIT 10;

SELECT
    `Product Name`,
    ROUND(SUM(`Order Profit Per Order`),2) AS profit
FROM supply_chain
GROUP BY `Product Name`
HAVING profit < 0
ORDER BY profit ASC
LIMIT 20;

SELECT
    `Product Name`,
    ROUND(SUM(Sales),2) AS revenue,
    ROUND(SUM(`Order Profit Per Order`),2) AS profit,
    ROUND(
        (SUM(`Order Profit Per Order`) * 100.0) /
        SUM(Sales),
        2
    ) AS profit_margin_pct
FROM supply_chain
GROUP BY `Product Name`
HAVING revenue > 10000
ORDER BY profit_margin_pct DESC
LIMIT 20;

SELECT
    COUNT(DISTINCT `Product Name`) AS total_products
FROM supply_chain;

SELECT
    `Product Name`,
    ROUND(SUM(Sales),2) AS revenue
FROM supply_chain
GROUP BY `Product Name`
ORDER BY revenue DESC;
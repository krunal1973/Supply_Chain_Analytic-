SELECT
    `Shipping Mode`,
    COUNT(*) AS orders
FROM supply_chain
GROUP BY `Shipping Mode`
ORDER BY orders DESC;

SELECT
    `Shipping Mode`,
    ROUND(SUM(Sales),2) AS revenue
FROM supply_chain
GROUP BY `Shipping Mode`
ORDER BY revenue DESC;

SELECT
    `Shipping Mode`,
    ROUND(SUM(`Order Profit Per Order`),2) AS profit
FROM supply_chain
GROUP BY `Shipping Mode`
ORDER BY profit DESC;

SELECT
    ROUND(
        AVG(
            DATEDIFF(
                `shipping date (DateOrders)`,
                `order date (DateOrders)`
            )
        ),
        2
    ) AS avg_shipping_days
FROM supply_chain;

SELECT
    `Delivery Status`,
    COUNT(*) AS orders
FROM supply_chain
WHERE `Delivery Status`='Late delivery'
GROUP BY `Delivery Status`;

SELECT
    `Delivery Status`,
    COUNT(*) AS orders
FROM supply_chain
WHERE `Delivery Status`='Shipping on time'
GROUP BY `Delivery Status`;

SELECT
    `Delivery Status`,
    COUNT(*) AS orders
FROM supply_chain
GROUP BY `Delivery Status`
ORDER BY orders DESC;

SELECT
    `Shipping Mode`,
    ROUND(AVG(`Order Item Product Price`),2) AS avg_price
FROM supply_chain
GROUP BY `Shipping Mode`;
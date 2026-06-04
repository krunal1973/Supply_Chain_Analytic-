SELECT Market,SUM(Sales) AS Total_Revenue
FROM supply_chain
GROUP BY Market
ORDER BY Total_Revenue DESC;


select Market,round(sum(`Order Profit Per Order`),2) as total_profit
from supply_chain
group by Market
order by total_profit desc;

select Market,count(distinct `Order Id`) as highest_orders 
from supply_chain
group by Market 
order by highest_orders desc ; 

select Market,round(sum(Sales)/count(distinct `Order Id`),2)
as Average_Order_Value from supply_chain
group by Market order by Average_Order_Value desc;


select Market,count(distinct `Customer Id`) 
as largest_customer_base from supply_chain 
group by market order by largest_customer_base desc;

SELECT Market,SUM(`Order Item Quantity`) 
AS total_products_sold FROM supply_chain
GROUP BY Market ORDER BY total_products_sold DESC;

select Market,round(sum(Sales) / 
(select sum(Sales) from supply_chain) * 100,2) 
as revenue_percentage from supply_chain
group by Market  order by revenue_percentage desc;

select Market,round(sum(Sales),2) 
as top_3_markets_by_revenue from supply_chain
group by Market order by top_3_markets_by_revenue desc limit 3; 

select Market,round(sum(`Order Profit Per Order`),2) 
as top_3_markets_by_Profit from supply_chain
group by Market order by top_3_markets_by_Profit desc limit 3;

select Order_Year,Order_Month,round(sum(Sales),2) 
as Market_Growth_Trend from supply_chain
group by Order_Year,Order_Month order by Order_Year,Order_Month;

SELECT
    Market,
    ROUND(
        SUM(
            CASE
                WHEN `Delivery Status` IN
                (
                    'Advance shipping',
                    'Shipping on time'
                )
                THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS delivery_performance_pct
FROM supply_chain
GROUP BY Market
ORDER BY delivery_performance_pct DESC;

SELECT
    Market,
    ROUND(AVG(Shipping_Delay), 2) AS avg_shipping_delay
FROM supply_chain
GROUP BY Market
ORDER BY avg_shipping_delay DESC;
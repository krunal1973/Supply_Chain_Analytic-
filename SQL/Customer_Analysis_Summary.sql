select `Customer Id`,`Customer Fname`,`Customer Lname`,ROUND(SUM(sales), 2) 
AS revenue from supply_chain 
group by `Customer Id`,`Customer Fname`,`Customer Lname`    
order by revenue desc limit 10 ;

select `Customer Id`,`Customer Fname`,`Customer Lname`,
round(sum(`Order Profit Per Order`),2) as profit
from supply_chain
group by `Customer Id`,`Customer Fname`,`Customer Lname`
order by profit desc limit 10;

select `Customer Country`,count(distinct `Customer Id`) 
as customers from supply_chain 
group by `Customer Country`
order by customers desc ;

SELECT
    customer_segment,
    COUNT(*) AS customers
FROM (
    SELECT
        `Customer Id`,
        CASE
            WHEN SUM(Sales) > 5000 THEN 'High Value'
            WHEN SUM(Sales) BETWEEN 2000 AND 5000 THEN 'Medium Value'
            ELSE 'Low Value'
        END AS customer_segment
    FROM supply_chain
    GROUP BY `Customer Id`
) t
GROUP BY customer_segment
ORDER BY customers DESC;

SELECT
    ROUND(SUM(Sales) / COUNT(DISTINCT `Customer Id`), 2) AS avg_revenue_per_customer
FROM supply_chain;


select customer_type, count(*) as customers 
from (
select `Customer Id`, case 
when count(distinct `Order Id`) = 1 then 'One-Time Customer'
else 'Repeat Customer'
end as customer_type
from supply_chain
group by `Customer Id` 
) t
group by customer_type;

SELECT
    `Customer Id`,
    `Customer Fname`,
    `Customer Lname`,
    COUNT(DISTINCT `Order Id`) AS total_orders
FROM supply_chain
GROUP BY
    `Customer Id`,
    `Customer Fname`,
    `Customer Lname`
ORDER BY total_orders DESC
LIMIT 10;

select `Customer Id`,
`Customer Fname`,`Customer Lname`,round(sum(Sales),2) 
as customer_lifetime_value from supply_chain 
group by `Customer Id`,
`Customer Fname`,`Customer Lname` 
order by customer_lifetime_value desc limit 10;
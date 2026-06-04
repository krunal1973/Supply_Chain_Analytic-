select count(distinct `Order Id`) 
as total_Orders
 from supply_chain ;
 
 select sum(sales) as total_revenue from supply_chain; 
 
 select sum(`Order Profit Per Order`) as total_profit 
 from supply_chain; 
 
 select count(distinct `Customer Id`) as total_customer from supply_chain; 
 
 select count(distinct `Product Card Id`) as total_Products from supply_chain;
 
 select round(sum(Sales) / count(distinct `Order Id`),2)
 as average_order_value  
 from supply_chain;
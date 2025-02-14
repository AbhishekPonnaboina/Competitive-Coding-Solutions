# Write your MySQL query statement below

Select p.product_name,sum(o.unit) as unit

From products p join orders o 
ON p.product_id = o.product_id
Where o.order_date between '2020-02-01' and '2020-02-29'

group by p.product_id having unit >= 100
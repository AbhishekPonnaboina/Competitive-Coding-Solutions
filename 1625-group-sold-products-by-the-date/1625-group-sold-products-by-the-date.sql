# Write your MySQL query statement below

Select sell_date,Count(Distinct product) as num_sold,
group_concat(Distinct product) as products

from Activities
group by sell_date
order by Sell_date
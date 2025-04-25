# Write your MySQL query statement below
with tt as 
    (SELECT person_name,weight,turn,sum(weight) over(order by turn)
        as total
    from Queue )
SELECT person_name 
from tt
where total <= 1000
order by total desc limit 1; 

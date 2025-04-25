# Write your MySQL query statement below

with tt as (
select id,num,lead(num,1) over (order by id) as seco , lead(num,2)  over (order by id) as third
from Logs )

select distinct (num) as ConsecutiveNums
from tt
where num = seco and num = third ;

# Write your MySQL query statement below

SELECT user_id,Concat(UPPER(left(name,1)),lOWER(right(name,length(name)-1))) as name

From Users
Order by user_id
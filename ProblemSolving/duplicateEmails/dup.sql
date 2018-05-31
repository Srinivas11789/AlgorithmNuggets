# Write your MySQL query statement below

select email from Person group by email having count(email) > 1
#select email,count(*) from Person group by email having count(email) > 1

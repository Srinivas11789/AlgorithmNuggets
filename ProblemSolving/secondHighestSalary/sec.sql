# Write your MySQL query statement below
select coalesce(
(select distinct a.salary from employee a group by salary desc limit 1 offset 1)) as SecondHighestSalary

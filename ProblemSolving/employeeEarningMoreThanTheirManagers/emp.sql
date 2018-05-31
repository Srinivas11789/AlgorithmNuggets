# Write your MySQL query statement below

select a.name "Employee" from employee a, employee b where a.ManagerId = b.id and b.salary < a.salary 

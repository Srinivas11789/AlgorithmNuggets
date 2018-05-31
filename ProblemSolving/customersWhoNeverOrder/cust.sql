# Write your MySQL query statement below

select name "Customers" from customers where id not in 
(select c.id from customers c, orders o where o.customerid = c.id)

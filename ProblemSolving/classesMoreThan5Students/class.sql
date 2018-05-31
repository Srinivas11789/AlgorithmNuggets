# Write your MySQL query statement below

select class from 
(select distinct student,class from courses) T 
group by class having count(class) >= 5

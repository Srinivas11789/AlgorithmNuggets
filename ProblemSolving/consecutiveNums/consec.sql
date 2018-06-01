# Write your MySQL query statement below


#select a.num from Logs group by num having count(num) >= 3 and case when count(num)*(count(num)+1)/2 = sum(select * from logs where num=a.num) 


select distinct a.num "ConsecutiveNums" from logs a, logs b, logs c where a.id = b.id-1 and b.id = c.id-1 and a.num = b.num and b.num = c.num

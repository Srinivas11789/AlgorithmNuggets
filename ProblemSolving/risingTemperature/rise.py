# Write your MySQL query statement below

select distinct a.id "Id" from weather a, weather b where b.RecordDate = DATE_SUB(a.RecordDate, INTERVAL 1 DAY) and a.temperature > b.temperature 

# Using date subtraction did not work
# select distinct a.id "Id" from weather a, weather b where a.recorddate = b.recorddate + 1 and a.temperature > b.temperature 

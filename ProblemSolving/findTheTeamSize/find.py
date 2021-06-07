# Write your MySQL query statement below

select e.employee_id, (select COUNT(team_id) from Employee where team_id=e.team_id) as team_size from Employee e;

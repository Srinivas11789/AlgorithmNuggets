# Write your MySQL query statement below

select case when id%2 = 0 then id - 1 
            when id%2 != 0 and id != (select max(id) from seat) then id + 1
            when id%2 != 0 and id = (select max(id) from seat) then id
            end as id, 
            student from seat order by 1
            
        

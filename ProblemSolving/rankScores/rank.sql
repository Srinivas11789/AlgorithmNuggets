# Write your MySQL query statement below

select s.score "Score", (select count(distinct score) from scores where score >= s.score ) Rank from scores s order by score desc

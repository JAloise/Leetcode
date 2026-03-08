# Write your MySQL query statement below
select e2.name as Employee
From employee e1 #Manager
INNER JOIN employee e2 #Employee
on e1.id = e2.managerId
where e2.salary > e1.salary

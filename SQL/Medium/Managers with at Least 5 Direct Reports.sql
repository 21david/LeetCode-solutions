# https://leetcode.com/problems/managers-with-at-least-5-direct-reports
# After seeing the editorial
with m as (
    # subquery to get groups of managerIds that appear more than 5 times
    select * from employee
    group by managerId
    having count(managerId) >= 5
)
# join to get the names of those managerIds
select e.name from employee e
join m
on e.id = m.managerId

/*
# Supplementary info on the table
Create table If Not Exists Employee (
    id int, 
    name varchar(255), 
    department varchar(255), 
    managerId int
)
Truncate table Employee
insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', NULL)
insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101')
insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101')
insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101')
insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101')
insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101')
*/

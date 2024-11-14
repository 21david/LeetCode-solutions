# https://leetcode.com/problems/primary-department-for-each-employee

# Using union:
# Employees in only one department
select employee_id, department_id
from employee
group by employee_id
having count(department_id) = 1

union

# Employees in more than one department
select employee_id, department_id
from employee
where primary_flag = 'Y'



# Using window:
# Add a column that tells us how many departments each employee is a part of, for each row
with window_table as (
    select
        *,
        count(*) over(partition by employee_id) as EmployeeCount
    from employee
)
select employee_id, department_id
from window_table
where EmployeeCount = 1 or primary_flag = 'Y'



# Using subquery and where:
select employee_id, department_id 
from employee e 
where (
    # Get the department count for this employee
    select count(department_id) 
    from employee 
    where employee_id = e.employee_id
) = 1
or primary_flag = 'y'

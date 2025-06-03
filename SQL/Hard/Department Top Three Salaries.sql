# Use window function to check what rank each salary has, which properly handles duplicates
with ranked as (
    select 
        name, 
        salary, 
        departmentId,
        dense_rank() over (partition by departmentId order by salary desc, departmentId) as rnk
    from employee e
)

# Select all salaries that have rank 1-3, along with department and employee name
select d.name as Department, r.name as Employee, salary as Salary
from ranked r
left join department d
    on r.departmentId = d.id
where rnk <= 3

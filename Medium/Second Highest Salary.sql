with ranked as (
    select
        *,
        dense_rank() over (order by salary desc) as rnk
    from employee
)
select salary as SecondHighestSalary
from ranked
where rnk = 2

# Add a null as default for if there is no second salary
union
select null
limit 1

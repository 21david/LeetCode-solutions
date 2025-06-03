select 
    employee_id,
    case
        when employee_id % 2 = 1 and name not like 'M%' then salary
        else 0
    end as bonus
from employees
order by employee_id



# Using regular expressions
select 
    employee_id,
    case
        when employee_id % 2 = 1 and name regexp '^[^M].*' then salary
        else 0
    end as bonus
from employees
order by employee_id



# or
select 
    employee_id,
    case
        when employee_id % 2 = 1 and name not regexp '^M.*' then salary
        else 0
    end as bonus
from employees
order by employee_id

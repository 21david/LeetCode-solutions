# https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee

select 
    c.reports_to as employee_id, 
    b.name, 
    count(c.reports_to) as reports_count, 
    round(avg(c.age), 0) as average_age
from employees c
join employees b
on c.reports_to = b.employee_id
group by c.reports_to
having count(c.reports_to) > 0
order by employee_id

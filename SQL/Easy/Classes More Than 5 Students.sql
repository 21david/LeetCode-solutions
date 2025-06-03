# https://leetcode.com/problems/classes-more-than-5-students

# Using having
select class 
from courses
group by class
having count(student) >= 5

  
# Using with
with counts as (
    select class, count(student) as count 
    from courses
    group by 1
)
select class 
from counts
where count >= 5

  
# Using subquery
select class
from (
    select class, count(student) as count
    from courses
    group by class
) as counts
where count >= 5


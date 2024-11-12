# https://leetcode.com/problems/classes-more-than-5-students

with counts as (
    select class, count(student) as count from courses
    group by 1
)
select class from counts
where count >= 5

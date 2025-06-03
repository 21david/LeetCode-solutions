# https://leetcode.com/problems/students-and-examinations

with counts as (
    select *, count(*) as a_e from examinations
    group by student_id, subject_name
) 
select s.student_id, s.student_name, sub.subject_name, ifnull(counts.a_e, 0) as attended_exams from students s
cross join subjects sub
left join counts on s.student_id = counts.student_id and sub.subject_name = counts.subject_name
order by student_id, subject_name

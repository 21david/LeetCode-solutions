# https://leetcode.com/problems/students-and-examinations

with counts as (
    select *, count(*) as a_e from examinations
    group by student_id, subject_name
) 
select s.student_id, s.student_name, sub.subject_name, ifnull(counts.a_e, 0) as attended_exams from students s
cross join subjects sub
left join counts on s.student_id = counts.student_id and sub.subject_name = counts.subject_name
order by student_id, subject_name



# Another solution:
-- Get all possible combinations of students and subjects
with combinations as (
    select student_id, student_name, subject_name
    from students st
    cross join subjects sb
),

-- Get counts of each subject test taken by each student
test_counts as (
    select student_id, subject_name, count(*) as counts
    from examinations
    group by student_id, subject_name
)

-- Left join to match counts of each subject taken to all possible combinations.
-- For resulting null values (student didnt take even 1 of that test), use ifnull() to make it 0
select 
    combinations.student_id, 
    student_name, 
    combinations.subject_name, 
    ifnull(test_counts.counts, 0) as attended_exams
from combinations
left join test_counts
    on combinations.student_id = test_counts.student_id
    and combinations.subject_name = test_counts.subject_name
order by combinations.student_id, combinations.subject_name

# https://leetcode.com/problems/patients-with-a-condition

select *
from patients
where conditions like 'diab1%' 
    or conditions like '% diab1%'



# Regex:
select *
from patients
where conditions regexp '^diab1| diab1'

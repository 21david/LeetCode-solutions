# https://leetcode.com/problems/biggest-single-number/

# Get all the single numbers
with singles as (
    select num
    from mynumbers
    group by num
    having count(num) = 1
)

# Get the highest one (returns null if table above is empty)
select max(num) as num
from singles

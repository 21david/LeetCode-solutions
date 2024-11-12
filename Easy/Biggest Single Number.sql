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


# Another approach
# Get all single numbers
select num
from mynumbers
group by num
having count(*) = 1

# Add null in case there are no single numbers
union
select null

# Take the top one
order by num desc
limit 1

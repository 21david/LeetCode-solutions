# https://leetcode.com/problems/fix-names-in-a-table
# concat(), left(), right(), upper(), lower(), length()

select
    user_id,
    concat(upper(left(name, 1)), lower(substring(name, 2))) as name
from users
order by user_id

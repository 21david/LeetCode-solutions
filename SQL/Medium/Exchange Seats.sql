# https://leetcode.com/problems/exchange-seats

select 
    case 
        when id % 2 = 1 and id = (
            select count(id) from seat
        ) then id 
        when id % 2 = 1 then id + 1
        else id - 1
    end as id,
    student
from seat
order by id

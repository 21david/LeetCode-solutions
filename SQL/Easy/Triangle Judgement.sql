# https://leetcode.com/problems/triangle-judgement
# Triangle can be formed if the two smaller added are bigger than the biggest side
  
select 
    *,
    case
        when (x + y + z) - greatest(x, y, z) > greatest(x,y,z) then 'Yes'
        else 'No'
    end as triangle
from triangle

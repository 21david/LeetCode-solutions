# O(N^3) time complexity
select distinct a.num as ConsecutiveNums
from logs a
cross join logs b
cross join logs c
where a.num = b.num and a.num = c.num 
    and a.id + 1 = b.id and a.id + 2 = c.id


# Equivalent syntactic sugar
select distinct a.num as ConsecutiveNums
from logs a, logs b, logs c
where a.num = b.num and a.num = c.num 
    and a.id + 1 = b.id and a.id + 2 = c.id

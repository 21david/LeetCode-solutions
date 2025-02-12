with inners as (
    select distinct p_id 
    from tree
    where p_id is not null
)
select
    id,
    case
        when p_id is null then 'Root'
        when id in (select * from inners) then 'Inner'
        else 'Leaf'
    end as type
from tree

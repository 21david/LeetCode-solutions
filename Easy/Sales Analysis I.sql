# using window function
with accumulated_sums_table as (
    select
        seller_id,
        sum(price) over (partition by seller_id) as acc
    from sales
) 
select distinct seller_id
from accumulated_sums_table
where acc = (select max(acc) from accumulated_sums_table)

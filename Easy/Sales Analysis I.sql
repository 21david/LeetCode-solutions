# using group by
select
    seller_id
from sales
group by seller_id
# Get the sellers that sold the max number of total price
having sum(price) = (
    # Get the maximum sum
    select
        sum(price)
    from sales
    group by seller_id
    order by 1 desc
    limit 1
);



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

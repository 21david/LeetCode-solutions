# Using group by
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



# Using window function with sum()
with accumulated_sums_table as (
    select
        seller_id,
        sum(price) over (partition by seller_id) as acc
    from sales
) 
select distinct seller_id
from accumulated_sums_table
where acc = (select max(acc) from accumulated_sums_table)

    

# Using window function with rank()
with ranked_sellers as (
    select
        seller_id,
        rank() over (order by sum(price) desc) as rnk
    from sales
    group by seller_id
)
select 
    seller_id
from ranked_sellers
where rnk = 1



/*
After seeing the optimal solution:
1. Aggregate sellers and their totals
2. Get the maximum total
3. Get the seller(s) with this maximum total
*/
with seller_totals as (
    select 
        seller_id,
        sum(price) as total
    from sales
    group by 1
)
select
    seller_id
from seller_totals
where total = (
    # Find max total
    select max(total)
    from seller_totals
)

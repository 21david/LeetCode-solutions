/*
We need the number of first orders which can be calculated just by the number of distinct customers.
We need all the first orders that were immediate orders (order_date == customer_pref_delivery_date and it was a first order)
Then we do the second result divide by the first, rounded to 2 decimal places.
*/

with first_immediates_count as (
    select count(*) as count
    from delivery
    where order_date = customer_pref_delivery_date
    and (customer_id, order_date) in (
        select customer_id, min(order_date)
        from delivery
        group by customer_id
    ) 
),
all_firsts_count as (
    select count(distinct customer_id) as count
    from delivery
)
select round((select count from first_immediates_count) / (select count from all_firsts_count) * 100, 2) as immediate_percentage



# With CTEs
select round(
    -- Total number of first orders that are immediate (numerator)
    (
        select count(*)
        from delivery
        where order_date = customer_pref_delivery_date
        and (customer_id, order_date) in (
            select customer_id, min(order_date)
            from delivery
            group by customer_id
        )
    )

    -- divided by
    / 

    -- Total number of first orders (denominator)
    (
        select count(distinct customer_id) 
        from delivery
    ) * 100,
    2
) as immediate_percentage 



# Shorter solution
select round(count(*) / (select count(distinct customer_id) from delivery) * 100, 2) as immediate_percentage
from delivery
where order_date = customer_pref_delivery_date
and (customer_id, order_date) in (
    -- get all first orders
    select customer_id, min(order_date)
    from delivery
    group by customer_id
) 

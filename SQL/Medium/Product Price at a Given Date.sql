with last_change_date as (
    select product_id, max(change_date)
    from products
    where datediff(change_date, '2019-08-16') <= 0
    group by product_id
)

-- products that changed price before or on 2019-08-16
select product_id, new_price as price
from products
where (product_id, change_date) in (
    select * 
    from last_change_date
)

union

-- products that didn't change price before or on 2019-08-16
select product_id, 10 as price
from products
where (product_id) not in (
    select product_id from (
        select * 
        from last_change_date
    ) p
)


# Sellers With No Sales (Premium LeetCode problem)
# MySQL
  
# Using subquery
select SELLER_NAME
from seller
where seller_id not in (
    select seller_id
    from orders
    where left(sale_date, 4) = '2020'
)
order by 1 asc

# Using Common Table Expression (CTE)
-- with orders_in_2020 as (
--     select * from orders
--     where left(sale_date, 4) = 2020
-- )
-- select SELLER_NAME
-- from seller
-- left join orders_in_2020 on seller.seller_id = orders_in_2020.seller_id
-- where order_id is null
-- order by 1 asc

# using window function
with accs as (
    select
        seller_id, price,
        sum(price) over (partition by seller_id) as acc_s
    from (
        select seller_id, price
        from sales s
        left join product p
        on s.product_id = p.product_id
    ) t
    order by price desc
)
select 
    distinct seller_id
from accs
where acc_s = (
    -- the sum of all sales of the best seller(s)
    select max(acc_s) from accs
)

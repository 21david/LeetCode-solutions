# https://leetcode.com/problems/list-the-products-ordered-in-a-period

select product_name, sum(unit) as unit
from orders o
left join products p
on p.product_id = o.product_id
where order_date between '2020-02-01' and '2020-02-29'
group by o.product_id
having sum(unit) >= 100

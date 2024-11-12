# https://leetcode.com/problems/product-sales-analysis-v/

select 
    user_id, 
    sum(quantity * price) as spending 
from sales s
left join product p
on s.product_id = p.product_id
group by user_id
order by spending desc, user_id

# https://leetcode.com/problems/average-selling-price

select p.product_id, round(sum(p.price * u.units) / sum(u.units), 2) as average_price 
from prices p
cross join unitssold u
where p.product_id = u.product_id
    and u.purchase_date between p.start_date and p.end_date
group by p.product_id

# products that were never sold
union
select product_id, 0 
from prices
where product_id not in (select product_id from unitssold)

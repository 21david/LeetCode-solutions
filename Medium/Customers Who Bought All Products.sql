# https://leetcode.com/problems/customers-who-bought-all-products
  
select customer_id
from customer
group by customer_id
having count(distinct product_key) = (
    # Get total number of products
    select count(distinct product_key) 
    from product
)

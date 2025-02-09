with ordered as (
    select distinct customerId
    from orders
)
select name as Customers
from customers
where id not in (select * from ordered)

with red_id as (
    select com_id
    from company
    where name = 'RED'
),
sold_red as (
    select distinct sales_id
    from orders
    where com_id = (select * from red_id)
)
select name
from salesperson
where sales_id not in (select * from sold_red)

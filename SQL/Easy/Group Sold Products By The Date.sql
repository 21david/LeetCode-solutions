## group_concat()
# https://www.w3resource.com/mysql/aggregate-functions-and-grouping/aggregate-functions-and-grouping-group_concat.php#SP

select 
    sell_date, 
    count(distinct product) as num_sold, 
    group_concat(distinct product order by product asc) as products
from activities
group by sell_date

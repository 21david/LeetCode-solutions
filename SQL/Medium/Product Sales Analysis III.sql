# https://leetcode.com/problems/product-sales-analysis-iii

# Get the first year for each product
with mins as (
    select mins.product_id, min(year) as first_year
    from sales mins
    group by product_id
)

# Fill in the rest of the information for each of those rows
select mins.product_id, mins.first_year, original.quantity, original.price
from mins
left join (
    select * from sales
) as original
on mins.product_id = original.product_id and mins.first_year = original.year



# Another approach, after seeing the editorial:
# select necessary rows from sales
# where (product_id, year) is in (sub query that gets first year for each product)

select product_id, year as first_year, quantity, price
from sales
where (product_id, year) in (
    select product_id, min(year)
    from sales
    group by 1
)

with app as (
    select 
        ifnull(country, 'null') as country,   -- 'null' string workaround to count nulls
        left(trans_date, 7) as month, 
        sum(amount) as approved_total_amount, 
        count(*) as approved_count
    from transactions
    where state = 'approved'
    group by country, month
), 
orig as (
    select 
        ifnull(country, 'null') as country, 
        left(trans_date, 7) as month, 
        sum(amount) as trans_total_amount, 
        count(*) as trans_count
    from transactions
    group by country, month
)
select 
    orig.month, 
    case 
        -- Undo the 'null' string workaround
        when orig.country = 'null' then null 
        else orig.country 
    end as country, 
    trans_count,
    ifnull(approved_count, 0) as approved_count,
    trans_total_amount,
    ifnull(approved_total_amount, 0) as approved_total_amount
from orig
left join app
on orig.country = app.country and orig.month = app.month

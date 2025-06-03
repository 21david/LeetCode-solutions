with approved as (
    select 
        ifnull(country, 'null') as country,   -- 'null' string workaround to count nulls
        left(trans_date, 7) as month, 
        sum(amount) as approved_total_amount, 
        count(*) as approved_count
    from transactions
    where state = 'approved'
    group by country, month
), 
original as (
    select 
        ifnull(country, 'null') as country, 
        left(trans_date, 7) as month, 
        sum(amount) as trans_total_amount, 
        count(*) as trans_count
    from transactions
    group by country, month
)
select 
    original.month, 
    case 
        -- Undo the 'null' string workaround
        when original.country = 'null' then null 
        else original.country 
    end as country, 
    trans_count,
    ifnull(approved_count, 0) as approved_count,
    trans_total_amount,
    ifnull(approved_total_amount, 0) as approved_total_amount
from original
left join approved
on original.country = approved.country and original.month = approved.month



# After seeing other's solutions:
select
    left(trans_date, 7) as month,
    country,
    count(id) as trans_count,
    sum(state = 'approved') as approved_count,  -- alternatively, sum(case when state = 'approved' then 1 else 0 end)
    sum(amount) as trans_total_amount,
    sum((state = 'approved') * amount) as approved_total_amount  -- alternatively, sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
group by country, month

# After seeing the editorial
select
    'Low Salary' as category,
    sum(case when income < 20000 then 1 else 0 end) as accounts_count
from accounts

union 

select
    'Average Salary' as category,
    sum(case when income between 20000 and 50000 then 1 else 0 end) as accounts_count
from accounts

union

select
    'High Salary' as category,
    sum(case when income > 50000 then 1 else 0 end) as accounts_count
from accounts




# First attempt
with final as (
    with categorized as (
        select
            case
                when income < 20000 then 'Low Salary'
                when income between 20000 and 50000 then 'Average Salary'
                else 'High Salary'
            end as category
        from accounts
    )
    select category, count(category) as accounts_count
    from categorized
    group by category

    # Add defaults in case they were missing
    union
    select 'Average Salary', 0

    union 
    select 'High Salary', 0

    union 
    select 'Low Salary', 0
)
# This part coalesces the default rows with actual rows. It removes duplicates.
select category, accounts_count
from final
group by category

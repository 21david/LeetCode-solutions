# After seeing a solution
# use if(condition, true_value, false_value) to turn actions into 1 or 0
# for each user_id, average all the confirmed's (1) with all the timeout's (0) to get the rate
# do a join or union to get users without any confirmations

# With left join:
select 
    s.user_id,
    round(avg(if(c.action = 'confirmed', 1, 0)), 2) as confirmation_rate
from signups s
left join confirmations c
on s.user_id = c.user_id
group by s.user_id


# With union:
with averages as (
    # Get averages from confirmations table
    select 
        c.user_id,
        round(avg(if(c.action = 'confirmed', 1, 0)), 2) as confirmation_rate
    from confirmations c
    group by c.user_id
)
# Add users who did not have any comfirmations
select 
    user_id, 
    0 as confirmation_rate
from signups
where user_id not in (select user_id from averages)
union
select * 
from averages

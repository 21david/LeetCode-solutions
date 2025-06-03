# Calculate total number of friends for each id
select id, sum(count) as num
from (
    # Number of times each id appears as a requester
    select requester_id as id, count(requester_id) as count
    from requestaccepted
    group by requester_id

    # Number of times each id appears as an accepter
    union all
    select accepter_id as id, count(accepter_id) as count
    from requestaccepted
    group by accepter_id
) sums
group by id

# Get the one with the most friends
order by num desc
limit 1

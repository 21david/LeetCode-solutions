select round(count(a.player_id) / (select count(distinct player_id) from activity), 2) as fraction 
from activity a
cross join activity b
where a.player_id = b.player_id and datediff(a.event_date, b.event_date) = -1
    and (a.player_id, a.event_date) in (
        select player_id, min(event_date)
        from activity
        group by player_id
    )

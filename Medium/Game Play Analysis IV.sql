select round(count(a.player_id) / (select count(distinct player_id) from activity), 2) as fraction 
from activity a
cross join activity b
where a.player_id = b.player_id and datediff(a.event_date, b.event_date) = -1
    and (a.player_id, a.event_date) in (
        select player_id, min(event_date)
        from activity
        group by player_id
    )



# Spaced out and comented
select round(
    -- numerator part, number of players who came back the second day
    (
        select count(a.player_id)
        from activity a
        cross join activity b
        where a.player_id = b.player_id and datediff(a.event_date, b.event_date) = -1
            and (a.player_id, a.event_date) in (
                select player_id, min(event_date)
                from activity
                group by player_id
            )
    )
    
    -- divided by
    / 
     
     -- denoiminator part, total number of players
    (
        select count(distinct player_id)
        from activity
    ), 

    -- rounded to 2 decimal places
    2) as fraction




# With CTEs
with numerator as (
    select count(a.player_id)
    from activity a
    cross join activity b
    where a.player_id = b.player_id and datediff(a.event_date, b.event_date) = -1
        and (a.player_id, a.event_date) in (
            select player_id, min(event_date)
            from activity
            group by player_id
        )
),
denominator as (
    select count(distinct player_id)
    from activity
)
select round((select * from numerator) / (select * from denominator), 2) as fraction
    

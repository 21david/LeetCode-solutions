# With GROUP BY and HAVING
select actor_id, director_id
from ActorDirector
group by actor_id, director_id
having count(timestamp) >= 3


# With a derived table
select grouped.actor_id, grouped.director_id 
from 
    (select actor_id, director_id, count(*) as ct
    from actordirector
    group by actor_id, director_id) grouped
where ct >= 3

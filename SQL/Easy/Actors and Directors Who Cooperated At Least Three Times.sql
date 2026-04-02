select grouped.actor_id, grouped.director_id 
from 
    (select actor_id, director_id, count(*) as ct
    from actordirector
    group by actor_id, director_id) grouped
where ct >= 3

with part_one as (
    select u.name as 'results'
    from movierating m
    left join users u on u.user_id = m.user_id 
    group by m.user_id
    order by count(*) desc, name
    limit 1
),
part_two as (
    select title as 'results'
    from movierating mr
    left join movies mv on mv.movie_id = mr.movie_id
    where created_at between '2020-02-01' and '2020-02-29'
    group by mr.movie_id
    order by avg(rating) desc, title
    limit 1
)

select * from part_one
union all
select * from part_two

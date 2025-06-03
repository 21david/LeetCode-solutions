select 
    round(
        min(
            sqrt(power(b.x - a.x, 2) + power(b.y - a.y, 2))
        ), 
    2) as shortest
from point2d a, point2d b
where !(a.x = b.x and a.y = b.y)

# https://leetcode.com/problems/delete-duplicate-emails

delete p1
from person p1
join person p2
where p1.email = p2.email and p1.id > p2.id



# Using a subquery:
delete from person
where id not in (
    # Get the minimum id in each group - the ones to be kept
    # Nested select is required to avoid error due to an SQL optimization reason
    select * from (
        select min(id)
        from person
        group by email
    ) as mins
)

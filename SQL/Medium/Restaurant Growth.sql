# Get 7th day, which is the 1st day that appears in the result
with seventh_day as (
    select date_add(min(visited_on), interval 6 day)
    from customer
),

# Get the total amounts for each 7 day period
total_amounts as (
    select 
        distinct visited_on, 

        # Get the sum of all 7 days
        (
            select sum(amount) from customer 
            where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on
        ) as amount

        from customer c  # Adding the c is what makes the subquery above work

        # Filter only days that have 6 days before them
        where visited_on >= (select * from seventh_day)
)

# Add the average column
select *, round(amount / 7, 2) as average_amount from total_amounts

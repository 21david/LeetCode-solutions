with calculated as (
    select pid, i.tiv_2015, i.tiv_2016, i.lat, i.lon, other_tiv_2015_count, other_city_count from insurance i

    # Get the number of other equivalent tiv_2015s
    left join (
        select tiv_2015, count(tiv_2015) as other_tiv_2015_count
        from insurance
        group by tiv_2015
    ) t
    on i.tiv_2015 = t.tiv_2015

    # Get the number of other equivalent cities
    left join (
        select lat, lon, count(lat + ',' + lon) as other_city_count
        from insurance
        group by lat, lon
    ) t2
    on i.lat = t2.lat and i.lon = t2.lon
)

# Get the sum of only the ones that meet the criteria
select round(sum(tiv_2016), 2) as tiv_2016 from calculated 
where other_tiv_2015_count > 1
and other_city_count = 1

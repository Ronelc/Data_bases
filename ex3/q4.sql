-- A reference table with the number of institutions located in each country,
-- and the geographical area in which it is located.
WITH temp(region, country, totalInst) AS (
    select region, country, sum(count)
    from institutions
             natural join authors
    group by region, country
    order by region
)
select region, country, totalInst as totalCount
from temp t1
where not exists(
        select *
        from temp t2
        where (t1.region = t2.region)
          and (t1.totalInst < t2.totalInst)
    )
order by region, country;
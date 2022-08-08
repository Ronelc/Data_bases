WITH temp(conference, num) AS (
    select conference, count(distinct year)
    from authors
    group by conference
    order by conference
)

select distinct name
from authors
         natural join temp
where authors.conference = temp.conference
  and temp.num > 9
order by name;

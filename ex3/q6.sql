with recursive recursiveTable(name, distance) as (
    values ('Noam Nisan', 0)
    union
    select distinct A1.name, distance + 1
    from recursiveTable T,
         authors A1,
         authors A2
    where distance < 2
      and A2.name = T.name
      and A2.conference = A1.conference
      and A2.year = A1.year
      and A1.count >= 1)

select distinct name
from recursiveTable
order by name;

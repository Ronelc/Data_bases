select distinct name
from (authors natural join conferences) A1
where not exists(
        select conference
        from (authors natural join conferences) A2
        where name = 'Noam Nisan'
          and area = 'ai'
          and conference not in (
            select conference
            from (authors natural join conferences) A3
            where A3.name = A1.name
        ))
order by name;
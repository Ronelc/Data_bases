select DISTINCT year, name
from authors A1
where (institution = 'Hebrew University of Jerusalem')
  and ( conference = 'focs')
  and (year >= 2000)
  and (year <= 2020)
  and not exists (
    select *
    from authors A2
    where (institution = 'Hebrew University of Jerusalem')
  and ( conference = 'focs')
  and (year >= 2000)
  and (year <= 2020)
  and (A1.count
    < A2.count)
  and (A1.year = A2.year)
    )

order by year, name;
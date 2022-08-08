select DISTINCT institution, name
from authors
         natural join institutions
         natural join conferences
where (country = 'il')
  and (adjustedcount >= 2)
  and ((area = 'ai') or (subarea = 'db'))
order by institution, name;
select region,
       CAST(count(DISTINCT institution) as float) /
       count(DISTINCT country) as insAvg
from institutions
group by region
order by region;
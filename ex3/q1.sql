select region, count(DISTINCT country) as countryCount
from institutions
group by region
order by region;

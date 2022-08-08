select name
from authors
         natural join conferences
where area = 'systems'
group by name
having sum(count) >1

intersect
select name
from authors
         natural join conferences
where area = 'systems'  and year >= 2014
group by name
having sum(count) >0
order by name;

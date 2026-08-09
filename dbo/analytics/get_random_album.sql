select album
from (select distinct album from music where album not like '%- Single')
order by random()
limit 1
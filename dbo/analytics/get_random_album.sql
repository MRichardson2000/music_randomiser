select album
from (select distinct album from music)
order by random()
limit 1
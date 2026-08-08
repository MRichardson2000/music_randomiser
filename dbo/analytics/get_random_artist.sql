select artist
from (select distinct artist from music)
order by random()
limit 1
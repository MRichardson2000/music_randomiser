with ranked_skips as (
	select
		song_name, 
		artist,
		album, 
		sum(skip_count) as total_skips,
		rank() over (order by sum(skip_count) desc) as rnk
	from music where skip_count is not null
	group by song_name, artist, album
)
select song_name,
	   artist,
	   album,
	   total_skips	
from ranked_skips
where rnk = 1
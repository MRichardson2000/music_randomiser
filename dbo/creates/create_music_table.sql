create table if not exists music (
    id serial primary key,
    song_name text not null,
    artist text not null,
    album text,
    genre text, 
    year integer,
    total_time integer,
    track_count integer,
    play_count integer,
    play_date_utc timestamptz,
    skip_count integer,
    release_date timestamptz
);
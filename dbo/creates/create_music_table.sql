create table if not exists music (
    id serial primary key,
    song_name text not null,
    artist text not null,
    album text,
    genre text, 
    year integer
);
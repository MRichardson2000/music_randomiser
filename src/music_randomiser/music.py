from datetime import datetime
from typing import Any, TypedDict, cast

KEY_MAP = {
    "Name": "song_name",
    "Artist": "artist",
    "Album": "album",
    "Genre": "genre",
    "Year": "year",
    "Total Time": "total_time",
    "Track Count": "track_count",
    "Play Count": "play_count",
    "Play Date UTC": "play_date_utc",
    "Skip Count": "skip_count",
    "Release Date": "release_date",
}


class Music(TypedDict, total=False):
    song_name: str
    artist: str
    album: str | None
    genre: str | None
    year: int | None
    total_time: int | None
    track_count: int | None
    play_count: int | None
    play_date_utc: datetime | str | None
    skip_count: int | None
    release_date: datetime | str | None


def parse_music(music_dict: dict[str, Any]) -> Music:
    parsed = {db_key: music_dict.get(xml_key) for xml_key, db_key in KEY_MAP.items()}
    return cast(Music, parsed)

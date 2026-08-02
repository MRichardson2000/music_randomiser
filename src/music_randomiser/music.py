from typing import TypedDict, Any, cast


KEY_MAP = {
    "Name": "song_name",
    "Artist": "artist",
    "Album": "album",
    "Genre": "genre",
    "Year": "year",
}


class Music(TypedDict, total=False):
    song_name: str
    artist: str
    album: str
    genre: str
    year: int | None


def parse_music(music_dict: dict[str, Any]) -> Music:
    parsed = {db_key: music_dict.get(xml_key) for xml_key, db_key in KEY_MAP.items()}
    return cast(Music, parsed)

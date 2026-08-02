import plistlib
from pathlib import Path
from music_randomiser.utils import XML_FILE
from typing import Any, Optional
import random
from music_randomiser.logger import get_logger
from music_randomiser.exceptions import ReadXmlError


logger = get_logger(__name__)


######################################################################
# Read XML File
######################################################################


def read_xml(file_path: Path = XML_FILE) -> dict[str, Any]:
    try:
        with open(file_path, "rb") as file:
            plist = plistlib.load(file)
            logger.debug("Successfully read XML file")
            return plist
    except Exception as e:
        logger.error("Failed to read xml file: %s", e, exc_info=True)
        raise ReadXmlError(f"Failed to read XML file due to: {e}")


######################################################################
# Artists
######################################################################


def view_all_artists() -> list[str]:
    artists: set[str] = set()
    tracks = read_xml().get("Tracks", {})
    for v in tracks.values():
        artists.add(v.get("Artist"))
    return sorted(artists)


def random_artist(n: int = 1) -> list[str]:
    random_artists: list[str] = []
    for _ in range(n):
        random_artists.append(random.choice(view_all_artists()))
    return random_artists


######################################################################
# Albums
######################################################################


def view_all_albums() -> list[str]:
    albums: set[str] = set()
    tracks = read_xml().get("Tracks", {})
    for v in tracks.values():
        albums.add(v.get("Album"))
    return sorted(albums)


def random_album(n: int = 1) -> list[str]:
    random_albums: list[str] = []
    for _ in range(n):
        random_albums.append(random.choice(view_all_albums()))
    return random_albums


def view_year_albums(specified_year: int = 2025) -> list[str]:
    albums: set[str] = set()
    tracks = read_xml().get("Tracks", {})
    for v in tracks.values():
        if not v.get("Release Date") or not v.get("Album"):
            continue
        if v.get("Release Date").year == specified_year:
            if " - Single" in v.get("Album"):
                continue
            albums.add(v.get("Album"))
    return sorted(albums)


def random_year_album(n: int = 1, year: int = 2026) -> list[str]:
    random_year_album: list[str] = []
    for _ in range(n):
        choice = random.choice(view_year_albums(year))
        random_year_album.append(choice)
    return random_year_album


######################################################################
# Singles
######################################################################


def view_singles() -> list[str]:
    singles: set[str] = set()
    tracks = read_xml().get("Tracks", {})
    for v in tracks.values():
        if v.get("Album") and " - Single" in v.get("Album"):
            singles.add(v.get("Album"))
    return sorted(singles)


def random_n_single(n: int = 1) -> list[str]:
    random_singles: list[str] = []
    for _ in range(n):
        random_singles.append(random.choice(view_singles()))
    return random_singles


######################################################################
# Analytics
######################################################################


def view_highest_skipped_songs() -> dict[str, int] | None:
    songs_skipped: dict[str, int] = {}
    tracks = read_xml().get("Tracks", {})
    for v in tracks.values():
        song_name = v.get("Name")
        skip_count = v.get("Skip Count")
        if song_name and skip_count and skip_count > 5:
            songs_skipped[song_name] = skip_count
    return songs_skipped


def view_last_played_date(
    song: Optional[str], album: Optional[str]
) -> dict[str, str] | None:
    chosen_song: dict[str, str] = {}
    chosen_album: dict[str, str] = {}
    tracks = read_xml().get("Tracks", {})
    for v in tracks.values():
        if song and v.get("Name") == song:
            song_date = v.get("Year")
            if not song_date:
                continue
            chosen_song[song] = song_date
        elif album and v.get("Album") == album:
            album_date = v.get("Year")
            if not album_date:
                continue
            chosen_album[album] = album_date
    if song:
        return chosen_song
    elif album:
        return chosen_album
    return None


def main() -> None:
    print(view_last_played_date(song=None, album=None))


if __name__ == "__main__":
    main()

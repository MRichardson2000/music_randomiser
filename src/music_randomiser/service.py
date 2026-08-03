import plistlib
from pathlib import Path
from music_randomiser.utils import XML_FILE
from typing import Any, Optional
import random
from music_randomiser.logger import get_logger
from music_randomiser.dbutils import execute_transaction
from music_randomiser.music import Music, parse_music
from music_randomiser.exceptions import ReadXmlError


logger = get_logger(__name__)


######################################################################
# DB Insertion
######################################################################


def process_and_store_library(file_path: Path = XML_FILE) -> None:
    """Deletes the DB first, then reads the XML library, parses all tracks, and bulk-inserts them into the db.
    Run this if I download a new xml file because I've added a lot to my library"""
    raw_plist = read_xml(file_path)
    tracks: dict[str, Any] = raw_plist.get("Tracks", {})
    music_records: list[Music] = [parse_music(track) for track in tracks.values()]
    truncate_sql = "truncate table music restart identity"
    insert_sql = """
        INSERT INTO music (
            song_name,
            artist,
            album,
            genre,
            year
        )
        VALUES (:song_name, :artist, :album, :genre, :year);
    """
    execute_transaction([(truncate_sql, None), (insert_sql, music_records)])
    logger.info("Successfully imported %d songs into database", len(music_records))


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
# Analytics
######################################################################


class MusicAnalytics:
    def view_all_artists(self) -> list[str]:
        artists: set[str] = set()
        tracks = read_xml().get("Tracks", {})
        for v in tracks.values():
            artists.add(v.get("Artist"))
        return sorted(artists)

    def view_random_artist(self, n: int = 1) -> list[str]:
        random_artists: list[str] = []
        for _ in range(n):
            random_artists.append(random.choice(self.view_all_artists()))
        return random_artists

    def view_all_albums(self) -> list[str]:
        albums: set[str] = set()
        tracks = read_xml().get("Tracks", {})
        for v in tracks.values():
            albums.add(v.get("Album"))
        return sorted(albums)

    def view_random_album(self, n: int = 1) -> list[str]:
        random_albums: list[str] = []
        for _ in range(n):
            random_albums.append(random.choice(self.view_all_albums()))
        return random_albums

    def view_year_albums(self, specified_year: int = 2025) -> list[str]:
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

    def view_random_year_album(self, n: int = 1, year: int = 2026) -> list[str]:
        random_year_album: list[str] = []
        for _ in range(n):
            choice = random.choice(self.view_year_albums(year))
            random_year_album.append(choice)
        return random_year_album

    def view_singles(self) -> list[str]:
        singles: set[str] = set()
        tracks = read_xml().get("Tracks", {})
        for v in tracks.values():
            if v.get("Album") and " - Single" in v.get("Album"):
                singles.add(v.get("Album"))
        return sorted(singles)

    def view_random_n_single(self, n: int = 1) -> list[str]:
        random_singles: list[str] = []
        for _ in range(n):
            random_singles.append(random.choice(self.view_singles()))
        return random_singles

    def view_highest_skipped_songs(self) -> dict[str, int] | None:
        songs_skipped: dict[str, int] = {}
        tracks = read_xml().get("Tracks", {})
        for v in tracks.values():
            song_name = v.get("Name")
            skip_count = v.get("Skip Count")
            if song_name and skip_count and skip_count > 5:
                songs_skipped[song_name] = skip_count
        return songs_skipped

    def view_last_played_date(
        self, song: Optional[str], album: Optional[str]
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
    process_and_store_library()


if __name__ == "__main__":
    main()

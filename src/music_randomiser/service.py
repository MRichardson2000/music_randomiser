import plistlib
from pathlib import Path
from music_randomiser.utils import XML_FILE
from typing import Any
from music_randomiser.logger import get_logger
from music_randomiser.dbutils import execute_transaction, fetch_result, load_sql_as_text
from music_randomiser.music import Music, parse_music
from music_randomiser.exceptions import ReadXmlError
from music_randomiser.utils import ANALYTICS_DBO


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
# Analytics - SQL
######################################################################
def get_random_artist() -> str:
    artist = fetch_result(load_sql_as_text(ANALYTICS_DBO, "get_random_artist.sql"))
    return artist[0]["artist"]


def get_random_album() -> str:
    album = fetch_result(load_sql_as_text(ANALYTICS_DBO, "get_random_album.sql"))
    return album[0]["album"]


def main() -> None:
    # process_and_store_library()
    print(get_random_album())


if __name__ == "__main__":
    main()

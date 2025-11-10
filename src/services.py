import plistlib
from pathlib import Path
from src.config import XML_FILE
from typing import Any, Union, Optional, cast
from datetime import datetime


class XmlReader:
    def __init__(self) -> None:
        pass

    def read_xml(self, file_path: Path = XML_FILE) -> Union[dict[str, Any], str]:
        try:
            with open(file_path, "rb") as file:
                plist = plistlib.load(file)
                return plist
        except Exception as e:
            return f"Failed to read XML file due to: {e}"

    def view_artists(self) -> list[str]:
        artists: set[str] = set()
        xml_file = XmlReader.read_xml(self)
        if isinstance(xml_file, dict):
            tracks = cast(dict[str, dict[str, Any]], xml_file.get("Tracks", {}))
            for v in tracks.values():
                artist = v.get("Artist")
                if artist:
                    artists.add(artist)
            return sorted(artists)
        else:
            print(xml_file)
            return []

    def view_albums(self) -> list[str]:
        albums: set[str] = set()
        xml_file = XmlReader.read_xml(self)
        if isinstance(xml_file, dict):
            tracks = cast(dict[str, dict[str, Any]], xml_file.get("Tracks", {}))
            for v in tracks.values():
                album = v.get("Album")
                if album:
                    albums.add(album)
            return sorted(albums)
        else:
            print(xml_file)
            return []

    def view_2025_albums(self) -> list[str]:
        albums: set[str] = set()
        xml_file = XmlReader.read_xml(self)
        if isinstance(xml_file, dict):
            tracks = cast(dict[str, dict[str, Any]], xml_file.get("Tracks", {}))
            for v in tracks.values():
                album = v.get("Album")
                year = v.get("Release Date")
                if (
                    isinstance(album, str)
                    and isinstance(year, datetime)
                    and year.year == 2025
                ):
                    if " - Single" in album:
                        continue
                    albums.add(album)
            return sorted(albums)
        else:
            print(xml_file)
            return []

    def view_2026_albums(self) -> Union[list[str], str]:
        albums: set[str] = set()
        xml_file = XmlReader.read_xml(self)
        if isinstance(xml_file, dict):
            tracks = cast(dict[str, dict[str, Any]], xml_file.get("Tracks", {}))
            for v in tracks.values():
                album = v.get("Album")
                year = v.get("Release Date")
                if (
                    isinstance(album, str)
                    and isinstance(year, datetime)
                    and year.year == 2026
                ):
                    if " - Single" in album:
                        continue
                    albums.add(album)
            return sorted(albums)
        else:
            print(xml_file)
            return []

    def view_highest_skipped_songs(self) -> dict[str, int] | None:
        songs_skipped: dict[str, int] = {}
        xml_file = XmlReader.read_xml(self)
        if isinstance(xml_file, dict):
            tracks = cast(dict[str, dict[str, Any]], xml_file.get("Tracks", {}))
            for v in tracks.values():
                song_name = v.get("Name")
                skip_count = v.get("Skip Count")
                if song_name and skip_count:
                    if skip_count > 5:
                        songs_skipped[song_name] = skip_count
            return songs_skipped

    def view_singles(self) -> Optional[list[str]]:
        singles: set[str] = set()
        xml_file = XmlReader.read_xml(self)
        if isinstance(xml_file, dict):
            try:
                tracks = cast(dict[str, dict[str, Any]], xml_file.get("Tracks", {}))
                for v in tracks.values():
                    album = v.get("Album")
                    if album and " - Single" in album:
                        singles.add(album)
                return sorted(singles)
            except Exception as e:
                raise e

    def view_last_played_date(
        self, song: Optional[str], album: Optional[str]
    ) -> dict[str, str] | None:
        chosen_song: dict[str, str] = {}
        chosen_album: dict[str, str] = {}
        xml_file = XmlReader.read_xml(self)
        if isinstance(xml_file, dict):
            try:
                tracks = cast(dict[str, dict[str, Any]], xml_file.get("Tracks", {}))
                for v in tracks.values():
                    if song and v.get("Name") == song:
                        song_played_date = v.get("Play Date UTC")
                        if song_played_date:
                            clean_datetime = datetime.strptime(
                                song_played_date, "%Y-%m-%dT%H:%M:%SZ"
                            )
                            formatted_date = clean_datetime.strftime(
                                "%A, %d %B %Y at %I:%M %P"
                            )
                            str_date = str(formatted_date)
                            chosen_song[song] = str_date
                    elif album and v.get("Album") == album:
                        album_played_date = v.get("Play Date UTC")
                        if album_played_date:
                            clean_datetime = datetime.strptime(
                                album_played_date, "%Y-%m-%dT%H:%M:%SZ"
                            )
                            formatted_date = clean_datetime.strftime(
                                "%A, %d %B %Y at %I:%M %P"
                            )
                            str_date = str(formatted_date)
                            chosen_album[album] = str_date
                            print(f"string dae: {str_date}")
                if song:
                    return chosen_song if chosen_song else None
                elif album:
                    return chosen_album if chosen_album else None
            except Exception as e:
                raise e
        return None


if __name__ == "__main__":
    reader = XmlReader()
    result = reader.view_last_played_date(song=None, album="Melancholy")
    print(result)

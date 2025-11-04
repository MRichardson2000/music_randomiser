import plistlib
from pathlib import Path
from src.config import XML_FILE
from typing import Any, Union, cast


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
            for _, v in tracks.items():
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
            for _, v in tracks.items():
                album = v.get("Album")
                if album:
                    albums.add(album)
            return sorted(albums)
        else:
            print(xml_file)
            return []


if __name__ == "__main__":
    reader = XmlReader()
    result = reader.view_albums()
    print(result)

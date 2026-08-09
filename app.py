######################################################################
# For use with Carnets on my iphone
######################################################################
import plistlib
from typing import Any, Optional
import random


######################################################################
# Exceptions
######################################################################
class MusicRandomiserError(Exception):
    """Base Exception for all music_randomiser errors"""

    pass


class ReadXmlError(MusicRandomiserError):
    """Raised when underlying database operations fail"""

    pass


######################################################################
# Read XML File
######################################################################


######################################################################
# Analytics
######################################################################
class MusicAnalytics:
    def __init__(self, file: str = "Library.xml") -> None:
        self.file = file

    def read_xml(self) -> dict[str, Any]:
        try:
            with open(self.file, "rb") as file:
                plist = plistlib.load(file)
                return plist
        except Exception as e:
            raise ReadXmlError(f"Failed to read XML file due to: {e}")

    def view_all_artists(self) -> list[str]:
        artists: set[str] = set()
        tracks = self.read_xml().get("Tracks", {})
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
        tracks = self.read_xml().get("Tracks", {})
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
        tracks = self.read_xml().get("Tracks", {})
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
        tracks = self.read_xml().get("Tracks", {})
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
        tracks = self.read_xml().get("Tracks", {})
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
        tracks = self.read_xml().get("Tracks", {})
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


######################################################################
# Entry point
######################################################################
def selector(opt: int, val: int) -> None:
    ma = MusicAnalytics()
    if opt == 1:
        print(ma.view_all_artists())
    elif opt == 2:
        print(ma.view_random_artist(val))
    elif opt == 3:
        print(ma.view_all_albums())
    elif opt == 4:
        print(ma.view_random_album(val))
    elif opt == 5:
        print(ma.view_year_albums(val))
    elif opt == 6:
        print(ma.view_random_year_album(val))
    elif opt == 7:
        print(ma.view_singles())
    elif opt == 8:
        print(ma.view_random_n_single(val))
    elif opt == 9:
        print(ma.view_highest_skipped_songs())
    elif opt == 10:
        print(ma.view_last_played_date(song="To The Hellfire", album=None))


def main():
    selector(2, 1)


if __name__ == "__main__":
    main()

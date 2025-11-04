import random
from src.services import XmlReader

environment = XmlReader()


def random_artist(times: int) -> str | None:
    for _ in range(times):
        artists = environment.view_artists()
        random_artist_selection = random.choice(artists)
        return random_artist_selection


def random_album(times: int) -> str | None:
    for _ in range(times):
        albums = environment.view_albums()
        random_album_selection = random.choice(albums)
        return random_album_selection


def main() -> None:
    pass


if __name__ == "__main__":
    pass

import random
from src.services import XmlReader

environment = XmlReader()


def random_artist(n: int = 2) -> list[str]:
    artist_list: list[str] = []
    random_artists: list[str] = []
    artists = environment.view_artists()
    for artist in artists:
        artist_list.append(artist)
    for _ in range(n):
        random_artists.append(random.choice(artist_list))
    return random_artists


def random_album(n: int = 5) -> list[str]:
    list_of_albums: list[str] = []
    random_albums: list[str] = []
    albums = environment.view_albums()
    for album in albums:
        list_of_albums.append(album)
    for _ in range(n):
        random_albums.append(random.choice(albums))
    return random_albums


def random_2025_album(n: int = 5) -> list[str]:
    list_of_albums: list[str] = []
    random_albums: list[str] = []
    albums = environment.view_2025_albums()
    for album in albums:
        list_of_albums.append(album)
    if albums:
        for _ in range(n):
            choice = random.choice(albums)
            random_albums.append(choice)
    return random_albums


def main() -> None:
    print(random_artist())
    print(random_album())
    print(random_2025_album())


if __name__ == "__main__":
    main()

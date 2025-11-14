import random
from src.services import XmlReader

environment = XmlReader()


def random_artist(n: int = 2) -> list[str]:
    list_of_artists: list[str] = []
    random_artists: list[str] = []
    artists = environment.view_artists()
    for artist in artists:
        list_of_artists.append(artist)
    for _ in range(n):
        random_artists.append(random.choice(list_of_artists))
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


def random_single(n: int = 20) -> list[str]:
    list_of_singles: list[str] = []
    random_singles: list[str] = []
    singles = environment.view_singles()
    if singles:
        for single in singles:
            list_of_singles.append(single)
    for _ in range(n):
        choice = random.choice(list_of_singles)
        random_singles.append(choice)
    return random_singles


def random_2025_album(n: int = 2) -> list[str]:
    list_of_albums: list[str] = []
    random_2025_album: list[str] = []
    albums = environment.view_2025_albums()
    for album in albums:
        list_of_albums.append(album)
    for _ in range(n):
        choice = random.choice(list_of_albums)
        random_2025_album.append(choice)
    return random_2025_album


def random_2026_album(n: int = 2) -> list[str]:
    list_of_albums: list[str] = []
    random_2026_album: list[str] = []
    albums = environment.view_2026_albums()
    for album in albums:
        list_of_albums.append(album)
    for _ in range(n):
        choice = random.choice(list_of_albums)
        random_2026_album.append(choice)
    return random_2026_album


def main() -> None:
    print(random_artist())
    print(random_album())
    print(random_single())
    print(random_2025_album())
    print(random_2026_album())


if __name__ == "__main__":
    main()

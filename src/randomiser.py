import random
from src.services import XmlReader

environment = XmlReader()


def random_artist(n: int = 2, year: int = 2025) -> list[str]:
    list_of_artists: list[str] = []
    artists_year: list[str] = []
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


def main() -> None:
    # print(random_artist())
    print(random_album(1))


if __name__ == "__main__":
    main()

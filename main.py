from src.randomiser import random_album, random_artist, random_2025_album
from src.services import XmlReader


def main():
    reader = XmlReader()
    print(reader.view_highest_skipped_songs())
    print(random_album())
    print(random_artist())
    print(random_2025_album())


if __name__ == "__main__":
    main()

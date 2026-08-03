from music_randomiser.service import MusicAnalytics


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

from song import Song

Song.count = 0
Song.genres = []
Song.artists = []
Song.genre_count = {}
Song.artist_count = {}

class TestSong:
    Song("99 Problems", "Jay Z", "Rap")
    Song("Halo", "Beyonce", "Pop")
    Song("Smells Like Teen Spirit", "Nirvana", "Rock")

    def test_saves_name_artist_genre(self):
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert(out_of_touch.name == "Out of Touch")
        assert(out_of_touch.artist == "Hall and Oates")
        assert(out_of_touch.genre == "Pop")

    def test_has_song_count(self):
        assert(Song.count == 4)
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert(Song.count == 5)

    def test_has_genres(self):
        assert("Rap" in Song.genres)
        assert("Pop" in Song.genres)
        assert("Rock" in Song.genres)

    def test_has_artists(self):
        assert("Jay Z" in Song.artists)
        assert("Beyonce" in Song.artists)
        assert("Hall and Oates" in Song.artists)
        
    def test_has_genre_count(self):
        assert(Song.genre_count["Rap"] == 1)
        assert(Song.genre_count["Pop"] == 3)
        assert(Song.genre_count["Rock"] == 1)

    def test_has_artist_count(self):
        assert(Song.artist_count["Jay Z"] == 1)
        assert(Song.artist_count["Beyonce"] == 1)
        assert(Song.artist_count["Nirvana"] == 1)
        assert(Song.artist_count["Hall and Oates"] == 2)


if __name__ == "__main__":
    test = TestSong()
    print("Running tests...")
    
    test.test_saves_name_artist_genre()
    print("✓ test_saves_name_artist_genre passed")
    
    test.test_has_song_count()
    print("✓ test_has_song_count passed")
    
    test.test_has_genres()
    print("✓ test_has_genres passed")
    
    test.test_has_artists()
    print("✓ test_has_artists passed")
    
    test.test_has_genre_count()
    print("✓ test_has_genre_count passed")
    
    test.test_has_artist_count()
    print("✓ test_has_artist_count passed")
    
    print("\n🎉 All tests passed!")

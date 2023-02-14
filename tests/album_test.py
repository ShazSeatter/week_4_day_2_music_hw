import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album("In The Lonely Hour", "Pop/Rock", "Sam Smith")
    
    def test_album_has_title(self):
        expected = 'In The Lonely Hour'
        actual = self.album.title
        self.assertEqual(expected, actual)

    def test_album_has_genre(self):
        expected = 'Pop/Rock'
        actual = self.album.genre
        self.assertEqual(expected, actual)

    def test_album_has_artist(self):
        expected = 'Sam Smith'
        actual = self.album.artist
        self.assertEqual(expected, actual)

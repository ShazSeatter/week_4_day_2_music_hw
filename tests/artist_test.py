import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Sam Smith")
    
    def test_artist_has_name(self):
        expected = 'Sam Smith'
        actual = self.artist.name
        self.assertEqual(expected, actual)

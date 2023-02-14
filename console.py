import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.select_all()
artist_repository.select_all()

artist_1 = Artist("Sam Smith")
artist_repository.save(artist_1)


album_1 = Album('In The Lonely Hour', 'Pop/Rock', artist_1)
album_repository.save(album_1)


pdb.set_trace()
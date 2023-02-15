import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


album_repository.select_all()
artist_repository.select_all()

artist_1 = Artist('Sam Smith')
artist_repository.save(artist_1)


album_1 = Album('In The Lonely Hour', 'Pop/Rock', artist_1)
album_repository.save(album_1)


for album in album_repository.select_all():
    print(album.__dict__)


for album in artist_repository.albums(artist_1):
    print(album.title)


pdb.set_trace()
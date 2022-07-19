"""Сделать запрос, который вернет нам артистов, у которых более 3 альбомов.
Запрос должен вернуть следующие поля:
- ArtistId
- ArtistName
- AlbumsCount
Для выполнения задания использовать базу данных Chinook_Sqlite.sqlite.
В качестве ORM используем SQLAlchemy."""

from sqlalchemy import create_engine, orm, func, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.exc import DatabaseError
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')

file_handler = logging.FileHandler('Log_HW23.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

Base = automap_base()

engine = create_engine(r"sqlite:///./Chinook_Sqlite.sqlite")
Base.prepare(engine, reflect=True)

if not inspect(engine).has_table("Album"):
    logger.error('table "Album" does not exists')
    raise FileExistsError('table "Album" does not exists')
else:
    Album = Base.classes.Album

if not inspect(engine).has_table("Artist"):
    logger.error('table "Artist" does not exists')
    raise FileExistsError('table "Artist" does not exists')
else:
    Artist = Base.classes.Artist

Session = orm.sessionmaker(engine)
session = Session()

cntAlbums = 3
CountAlbum = func.count(Album.ArtistId).label("CountAlbum")

result = (session.query(Album.ArtistId, CountAlbum, Artist.Name)
          .join(Artist, Artist.ArtistId == Album.ArtistId)
          # .filter(Album.ArtistId.in_([16, 17]))
          .group_by(Album.ArtistId, Artist.Name).having(CountAlbum > cntAlbums).all())
logger.info(f'For count albums more {cntAlbums} result is {result}')
for ArtistId, CountAlbum, ArtistName in result:
    print('ArtistId: ', ArtistId, '  cntAlbum: ', CountAlbum, '  ArtistName: ', ArtistName)


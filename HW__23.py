"""Сделать запрос, который вернет нам артистов, у которых более 3 альбомов.
Запрос должен вернуть следующие поля:
- ArtistId
- ArtistName
- AlbumsCount
Для выполнения задания использовать базу данных Chinook_Sqlite.sqlite.
В качестве ORM используем SQLAlchemy."""
# , {"cntAlbums": 4}

from sqlalchemy import text
from sqlalchemy import create_engine
engine = create_engine(r"sqlite:///./Chinook_Sqlite.sqlite")


with engine.connect() as conn:
    cntAlbums = 3
    result = conn.execute(text(
        "select  a.ArtistId, a.Name as ArtistName, count(AlbumId) as cntAlbum from Artist  as a "
        "join Album as al on a.ArtistId = al.ArtistId group by a.ArtistId, a.Name having count(AlbumId) > :cntAlbums "
        "order by count(AlbumId) desc").bindparams(cntAlbums=cntAlbums))
    for row in result:
        print(f"ArtistId: {row.ArtistId}  ArtistName: {row.ArtistName}  cntAlbum: {row.cntAlbum}")

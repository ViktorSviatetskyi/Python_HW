"""Сделать запрос, который вернет нам артистов, у которых более 3 альбомов.
Запрос должен вернуть следующие поля:
- ArtistId
- ArtistName
- AlbumsCount

Для выполнения задания использовать базу данных Chinook_Sqlite.sqlite."""


import sqlite3
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger1 = logging.getLogger("Err")
logger1.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')

file_handler = logging.FileHandler('Log_HW22.log')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger1.addHandler(file_handler)
logger1.addHandler(stream_handler)


conn = sqlite3.connect("Chinook_Sqlite.sqlite")

cursor = conn.cursor()
cntAlbums = 3
try:
    cursor.execute(
        "select  a.ArtistId, a.Name as ArtistName, count(AlbumId) as cntAlbum from Artist  as a "
        f"join Album as al on a.ArtistId = al.ArtistId group by a.ArtistId, a.Name having count(AlbumId) > {cntAlbums} "
        "order by count(AlbumId) desc")
    result = cursor.fetchall()
    logger.info(f'For count albums more {cntAlbums} result is {result}')
    for ArtistId, ArtistName,  cntAlbum in result:
        print('ArtistId: ', ArtistId, 'ArtistName: ', ArtistName, '         cntAlbum: ', cntAlbum)
except sqlite3.DatabaseError as err:
    logger1.exception('Error')
else:
    conn.commit()


conn.close()

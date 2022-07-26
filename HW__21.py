"""Написать скрипт, который, используя asyncio и aiohttp, скачивает набор файлов из сети.
Файлов не должно быть меньше 20."""


import time
import os
import logging
import shutil
import asyncio
import aiohttp
import aiofiles
from aiologger import Logger

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')

file_handler = logging.FileHandler('Log_HW21.log')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

img_urls = [
    'https://images.unsplash.com/photo-1454496522488-7a8e488e8606?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80',
    'https://images.unsplash.com/photo-1542662565-7e4b66bae529?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=627&q=80',
    'https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80 ',
    'https://images.unsplash.com/photo-1574950578143-858c6fc58922?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
    'https://images.unsplash.com/photo-1501785888041-af3ef285b470?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',
    'https://images.unsplash.com/photo-1506106487742-2baf007edcfb?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
    'https://images.unsplash.com/photo-1447433589675-4aaa569f3e05?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80',
    'https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',
    'https://images.unsplash.com/photo-1529788295308-1eace6f67388?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1171&q=80',
    'https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=671&q=80',
    'https://images.unsplash.com/photo-1543722530-d2c3201371e7?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1174&q=80',
    'https://images.unsplash.com/photo-1536904132820-d4760eae1463?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=688&q=80',
    'https://images.unsplash.com/photo-1462331940025-496dfbfc7564?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=911&q=80',
    'https://images.unsplash.com/photo-1567095761054-7a02e69e5c43?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
    'https://images.unsplash.com/photo-1640074130674-146cf793baac?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=627&q=80',
    'https://images.unsplash.com/photo-1610422285430-9b445aeb3b72?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1yZWxhdGVkfDEwfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60',
    'https://images.unsplash.com/photo-1549849171-09f62448709e?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',
    'https://images.unsplash.com/photo-1556103727-777acb371272?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80',
    'https://images.unsplash.com/photo-1470092306007-055b6797ca72?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
    'https://images.unsplash.com/photo-1587059481645-b3a17becd6e0?ixlib=rb-1.2.1&ixid'
    '=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=765&q=80 '
]

t1 = time.perf_counter()


def create_recreate_dir(dir_path: str):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        logger.info(f'New dir {dir_path} was created')
    else:
        shutil.rmtree(dir_path)
        logger.info(f'Dir {dir_path} already exists and was deleted')
        os.makedirs(dir_path)
        logger.info(f'Dir {dir_path} was created again')


img_path = "./HW_21_Images/async/"


async def download_images(img_url):

    img_name = img_url.split('/')[3][0:19]
    img_name = f'{img_path}{img_name}.jpg'
    async with aiohttp.ClientSession() as session:
        async with session.get(img_url) as resp:
            assert resp.status == 200
            data = await resp.read()

    async with aiofiles.open(
        os.path.join(img_name), "wb"
    ) as outfile:
        await outfile.write(data)
        logger.debug(f"Download: {img_name}")

if __name__ == "__main__":
    create_recreate_dir(img_path)
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(download_images(url)) for url in img_urls]
    loop.run_until_complete(asyncio.wait(tasks))

    t2 = time.perf_counter()
    print(f'Finished in {round(t2-t1)} seconds')

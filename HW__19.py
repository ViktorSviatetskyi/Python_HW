"""Написать скрипт, который используя мультипроцесность, скачивает набор файлов из сети.
Файлов не должно быть меньше 20.
Для реализации функционала требуется использовать concurrent.futures.ProcessPoolExecutor."""
import time
import requests
import os
import concurrent.futures
import logging
import shutil


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')

file_handler = logging.FileHandler('Log_HW19.log')
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


img_path = "./HW_18_19_Images/Process/"


def download_images(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3][0:19]
    img_name = f'{img_path}{img_name}.jpg'
    if not os.path.exists(img_name):
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
            logger.info(f'{img_name} was downloaded')
    else:
        logger.info(f'file {img_name} already exists')


if __name__ == "__main__":
    create_recreate_dir(img_path)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_images, img_urls)

    t2 = time.perf_counter()
    print(f'Finished in {round(t2-t1)} seconds')

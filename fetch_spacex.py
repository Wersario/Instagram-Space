import os
import requests
from PIL import Image


def get_link_expansion(link):
    separated_link = link.split('.')
    return '.' + separated_link[-1]


def resize_picture(path):
    image = Image.open(path)
    image.thumbnail((1080, 1080))
    image.convert('RGB').save(f'{path.split(".")[0]}.jpg')
    if get_link_expansion(path) != '.jpg':
        os.remove(path)


def download_image(url, path):
    os.makedirs("images", exist_ok=True)
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path, "wb") as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    os.makedirs("images", exist_ok=True)
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()
    for count, link in enumerate(response.json()['links']['flickr']['original']):
        download_image(link, f'images/spacex{count}.jpg')
        resize_picture(f'images/spacex{count}.jpg')


fetch_spacex_last_launch()

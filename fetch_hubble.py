import os
import requests
from PIL import Image


def get_link_expansion(link):
    split_link = link.split('.')
    return '.' + split_link[-1]


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


def fetch_hubble_id_photos(image_id, number):
    os.makedirs("images", exist_ok=True)
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    image = response.json()['image_files'][-1]
    download_image(f"https:{image['file_url']}", f"images/hubble{image_id}_{number}{get_link_expansion(image['file_url'])}")
    resize_picture(f"images/hubble{image_id}_{number}{get_link_expansion(image['file_url'])}")

import requests
import os
import shutil
from PIL import Image
from instabot import Bot
from dotenv import load_dotenv
from os import listdir


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


def fetch_spacex_last_launch():
    os.makedirs("images", exist_ok=True)
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()
    for count, i in enumerate(response.json()['links']['flickr']['original']):
        download_image(i, f'images/spacex{count}.jpg')
        resize_picture(f'images/spacex{count}.jpg')


def fetch_hubble_id_photos(image_id, number):
    os.makedirs("images", exist_ok=True)
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    image = response.json()['image_files'][-1]
    download_image(f"https:{image['file_url']}", f"images/hubble{image_id}_{number}{get_link_expansion(image['file_url'])}")
    resize_picture(f"images/hubble{image_id}_{number}{get_link_expansion(image['file_url'])}")


load_dotenv()
shutil.rmtree('config')
bot = Bot()
bot.login(username=os.getenv("INSTA_LOGIN"), password=os.getenv("INSTA_PASSWORD"))

fetch_spacex_last_launch()
for number, photo_path in enumerate(listdir('images')):
    bot.upload_photo(f'images/{photo_path}', caption=f'Beatiful space photo number {number}')


# все, что ниже, используется для чистки лиших файлов
for item in os.listdir('images'):
    if item.endswith(".REMOVE_ME"):
        os.remove(item)

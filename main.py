import os
import shutil
from instabot import Bot
from dotenv import load_dotenv
from os import listdir


load_dotenv()
if os.path.exists('config'):
    shutil.rmtree('config')
bot = Bot()
bot.login(username=os.getenv("INSTA_LOGIN"), password=os.getenv("INSTA_PASSWORD"))

for number, photo_path in enumerate(listdir('images')):
    bot.upload_photo(f'images/{photo_path}', caption=f'Beatiful space photo number {number}')


# все, что ниже, используется для чистки лиших файлов
for item in os.listdir('images'):
    if item.endswith(".REMOVE_ME"):
        os.remove(f'images/{item}')

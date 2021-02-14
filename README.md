# Космический Инстаграм

### О проекте
С помощью данного кода вы сможете скачивать фотографии о космосе в ваш инстраграм.
Их можно брать с последних запусков SpaceX или из коллекций телескопа Hubble.
 
### Как установить
1. Создайте файл `.env` и положите ваши пароль и логин от инстаграма в переменные `INSTA_LOGIN` и `INSTA_PASSWORD`. Пример: 
    ```
    INSTA_LOGIN=dvmncool@mail.ru
    INSTA_PASSWORD=12345
    ```

2. Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
    ```
    pip install -r requirements.txt
    ```

### Дополнительная информация
Узнать о API SpaceX вы можете на [documenter.getpostman.com](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1).

О API Hubble на [hubblesite.org](http://hubblesite.org/api/documentation).

О том как пользоваться instabot на [instagrambot.github.io](https://instagrambot.github.io/docs/en/For_developers.html#photos).

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
from pprint import pprint

import requests
from bs4 import BeautifulSoup

# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'сервер', 'Москва', 'Java', 'C++']

URL = 'https://habr.com/ru/all/'
response = requests.get(URL)
if response.status_code != 200:
    raise RuntimeError('Сервер не доступен')

soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('article', class_='post post_preview')
for post in posts:
    post_text = post.find('div', class_='post__text post__text-html post__text_v1')
    if post_text is None:
        post_text = post.find('div', class_='post__text post__text-html post__text_v2')

    for word in KEYWORDS:
        if word in post_text.text:
            time = post.find('span', class_='post__time').text
            title = post.find('h2', class_='post__title').text
            url = post.find('a', class_='post__title_link').attrs.get('href')
            print(time.strip(), ' - ', title.strip(), ' - ', url)
            break


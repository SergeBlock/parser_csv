# высылка запроса и преоразование в суп
import csv
import json

import requests
from bs4 import BeautifulSoup

from config import products_list

products_list = products_list


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    with open('index.html', 'w') as file:
        file.write(r.text)
        file.close()
    return soup


# получение данных из супа
def parse(soup):
    # productslist = []
    global products_list
    result = soup.find_all('article', {
        'class': 'cldt-summary-full-item listing-impressions-tracking list-page-item ListItem_article__ppamD'})

    for item in result:
        product = {'name': item.find('h2').text + item.find('span', {'class': 'ListItem_version__jNjur'}).text,
                   'ID': item['id'],
                   'href': item.find('a', {'class': 'ListItem_title__znV2I Link_link__pjU1l'})['href']
                   }
        products_list.append(product)

    return products_list


# Высылка сообщение ботом
def send_message(chat_id, message):
    get_messanger = {'chat_id': chat_id,
                     'text': message
                     }
    chat = requests.get(
        f'https://api.telegram.org/bot1341365211:AAFUF_x74D8zxeFGRcCu6e2HuprexA-z9IM/sendMessage?chat_id={chat_id}&text=https://www.autoscout24.de{message}')
    return chat


def save(product_list, path):  # ФУНКЦИЯ ЗАПИСИ
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Name', 'ID', 'href'))  # заголовоки таблицы
        for team in product_list:
            writer.writerow((team['name'], team['ID'], team['href']))
        csvfile.close()

# сохранение в json
def save_json(product_list, path):
    with open(path,'w') as file:
        json.dump(product_list,file,indent=4, ensure_ascii=False)
        file.close()




# из файла в словарь
def file_to_dict(path):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        alt_list = []
        for row in reader:
            product = {'name': row['Name'],
                       'ID': row['ID'],
                       'href': row['href']

                       }
            alt_list.append(product)
        csvfile.close()
    return alt_list


# достает все айди из файла в список
def get_ids(path):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        ids = []
        for row in reader:
            ids.append(row['ID'])
    csvfile.close()
    return ids

# while open('alt_product_list.json',  'r') as file:
#         alt_product_list = json.load(file)
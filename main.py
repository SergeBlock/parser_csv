import csv
import json

import requests
from bs4 import BeautifulSoup

url = 'https://www.autoscout24.de/lst/volkswagen/caddy/ve_maxi?fregfrom=2010&sort=age&desc=1&cy=D&atype=C&ustate=N%2CU&powertype=kw&ocs_listing=include&amp%3Bdesc=0&amp%3Bustate=N%2CU&amp%3Batype=C&amp%3Bcy=D&amp%3Bocs_listing=include&amp%3Bfregfrom=2010&search_id=qf54cm5goi&page='

chat_id = '142106628'

products_list = []

# высылка запроса и преоразование в суп
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



if __name__ == '__main__':
    for i in range(1,21):
        list_url = url + str(i)
        print('SOUP')
        soup = get_data(list_url)
        print('parse')
        parse(soup)

    # with open('alt_product_list.json') as file:
    #     alt_product_list = json.load(file)
    #     file.close()
    #
    #
    # for i in products_list:
    #     for j in alt_product_list:
    #         if i['ID'] != j['ID']:
    #             send_message(chat_id, i['href'])





    ids = get_ids('alt_product_list.csv')

    for i in products_list:
        if i['ID'] not in ids:
            send_message(chat_id, i['href'])
    print('Speichern')
    save(products_list, 'alt_product_list.csv')

    # save_json(products_list,'alt_product_list.json')


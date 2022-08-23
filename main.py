from autoscout import *
from config import products_list, chat_id, url


def main():
    global list_url
    for i in range(1,21):
        list_url = url + str(i)
        print('SOUP')
        soup = get_data(list_url)
        print('parse')
        parse(soup)


    ids = get_ids('alt_product_list.csv')

    for i in products_list:
        if i['ID'] not in ids:
            send_message(chat_id, i['href'])
    print('Speichern')
    save(products_list, 'alt_product_list.csv')

    # save_json(products_list,'alt_product_list.json')



if __name__ == '__main__':
    main()


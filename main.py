from autoscout import *
from config import *
from mobile import *


def main():
    #     парсер скоут24.де
    for i in range(1, 21):
        list_url = url_scout + str(i)
        soup = get_data(list_url)
        parse_scout(soup)
        print('заполняю скоут')

    ids = get_ids('alt_product_list.csv')
    for i in products_list:
        if i['ID'] not in ids:
            send_message(chat_id, i['href'])
            print('новая скоут')
        save(products_list, 'alt_product_list.csv')

    # парсер мобиль.де
    for i in range(1, 14):
        url = url_mobile1 + str(i) + url_mobile2
        soup = get_data_mobile(url)
        parser_mobile(soup)
        ids = get_ids('alte_product_list_mobile.csv')
        print('заполняю мобиле')

    for product in products_list_mobile:
        if product['ID'] not in ids:
            send_message_mobile(chat_id, product['href'])
            print('новая мобиле')
    save(products_list_mobile, 'alte_product_list_mobile.csv')




if __name__ == '__main__':
    main()

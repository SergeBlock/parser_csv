from autoscout import *

url = 'https://www.autoscout24.de/lst/volkswagen/caddy/ve_maxi?fregfrom=2010&sort=age&desc=1&cy=D&zipr=150&zip=53117%20Zentrum%20%28Bonn%29&lon=7.0709135&lat=50.7578523&atype=C&ustate=N%2CU&powertype=kw&priceto=17500&ocs_listing=include&amp%3Bdesc=0&amp%3Bustate=N%2CU&amp%3Batype=C&amp%3Bcy=D&amp%3Bocs_listing=include&amp%3Bfregfrom=2010&search_id=49pe6bnzx8&page='

chat_id = '142106628'

products_list = []



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


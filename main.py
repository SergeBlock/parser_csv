from config import url_mobile
from mobile import *



def main():
    soup = get_data_mobile(url_mobile)
    parser_mobile(soup)
    print(products_list_mobile)

if __name__ == '__main__':
    main()

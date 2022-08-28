import time

from bs4 import BeautifulSoup
from selenium import webdriver


def get_data_mobile(url):
    # эмуляция браузера
    browser = webdriver.Chrome('/home/serge/PycharmProjects/parser/Chrome/chromedriver')
    # запуск браузера, запись в файл и обработка ошибок если есть
    try:
        browser.get(url=url)
        time.sleep(5)

        with open('index_selenium.html','w') as file:
            file.write(browser.page_source)
            file.close()
    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()

    #  готовка супа
        with open('index_selenium.html') as file:
            html = file.read()
            file.close()

    soup = BeautifulSoup(html, 'lxml')
    return soup



def parser_mobile(soup):
    global products_list_mobile
    result = soup.find_all('div',{'class': 'cBox-body cBox-body--resultitem'})
    for item in result:
        product = {'name':item.find('span',{'class', 'h3 u-text-break-word'}).text,
                    'ID': item.find('a',{'class':'link--muted no--text--decoration result-item'})['data-listing-id'],
                    'href': item.find('a',{'class':'link--muted no--text--decoration result-item'})['href']
              }
        products_list_mobile.append(product)
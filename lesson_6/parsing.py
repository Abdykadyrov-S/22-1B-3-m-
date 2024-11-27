from bs4 import BeautifulSoup
import requests

# response = requests.get(url='https://www.nbkr.kg/index.jsp?lang=RUS')

# response_text = BeautifulSoup(response.text, 'lxml')

# course = response_text.find_all('table', class_='table table-striped')

# for i in course:
#     print(i.text)


def parsing_sulpak():
    response = requests.get(url='https://www.sulpak.kg/')
    response_text = BeautifulSoup(response.text, 'lxml')
    products = response_text.find_all('div', class_='home__slider-product-inner')

    for i in products:
        print(i.text, end=" ")

parsing_sulpak()


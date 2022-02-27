from bs4 import BeautifulSoup
import requests
import re


class Parser:
     html = ""

     def __init__(self, url):
         self.url = url

     def get_html(self):
         req = requests.get(self.url).text
         self.html = BeautifulSoup(req, 'lxml')

     def parsing(self):
         elements = self.html.find_all("div", class_="model-price-range")  # []
         prices = []
         for element in elements:
             pr1 = element.find_all('span')[0].text
             price_1 = re.sub(r"\D", "", pr1)
             pr2 = element.find_all('span')[1].text
             price_2 = re.sub(r"\D", "", pr2)
             if price_2.isnumeric():  # содержит ли строка только числа
                 prices.append((int(price_1) + int(price_2)) / 2)
             else:
                 prices.append(int(price_1))

         print(prices)
         print(f"Средняя цена: {round(sum(prices) / len(prices))} руб.")

     def run(self):
         self.get_html()
         self.parsing()


pars = Parser(f"https://www.e-katalog.ru/list/206/")
pars.run()

from bs4 import BeautifulSoup
import requests
import re


class Parser:
     html = ""

     def __init__(self, url):
         self.url = url

     def get_html(self):
         req = requests.get(self.url).text
         self.html = BeautifulSoup(req, 'lxml')

     def parsing(self):
         elements = self.html.find_all("div", class_="model-price-range")  # []
         prices = []
         for element in elements:
             pr1 = element.find_all('span')[0].text
             price_1 = re.sub(r"\D", "", pr1)
             pr2 = element.find_all('span')[1].text
             price_2 = re.sub(r"\D", "", pr2)
             if price_2.isnumeric():  # содержит ли строка только числа
                 prices.append((int(price_1) + int(price_2)) / 2)
             else:
                 prices.append(int(price_1))
         return sum(prices) / len(prices)

     def run(self):
         self.get_html()
         return self.parsing()


av = []
for i in range(18):
    pars = Parser(f"https://www.e-katalog.ru/list/206/{i}/")
    av.append(pars.run())

print(av)
print(f"Средняя цена: {round(sum(av) / len(av), 2)} руб.")
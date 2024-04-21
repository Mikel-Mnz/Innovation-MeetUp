from flask import Flask, render_template, request, send_file
import requests
import pandas as pd
from bs4 import BeautifulSoup

app = Flask(__name__)

# Variable global para almacenar los datos raspados
dataList = []


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    global dataList
    baseurl_1 = "https://www.cyberpuerta.mx/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    all_productlinks = []

    for x in range(1, 7):
        r = requests.get(
            f'https://www.cyberpuerta.mx/Computo-Hardware/Servidores/Servidores/{x}')
        soup = BeautifulSoup(r.content, 'lxml')

        productList = soup.find_all(
            'li', class_='cell productData small-12 small-order-1')

        productList_2 = soup.find_all(
            'li', class_='cell productData small-12 small-order-3')

        productlinks = []

        for item in productList:
            for link in item.find_all('a', href=True):
                if link['href'].startswith('https://www.cyberpuerta.mx/Computo-Hardware/Servidores/Servidores/'):
                    productlinks.append(link['href'])

        for item in productList_2:
            for link in item.find_all('a', href=True):
                if link['href'].startswith('https://www.cyberpuerta.mx/Computo-Hardware/Servidores/Servidores/'):
                    productlinks.append(link['href'])

        all_productlinks.extend(productlinks)

    all_productlinks = list(set(all_productlinks))

    dataList = []
    for link in all_productlinks:

        r = requests.get(link, headers=headers)

        soup = BeautifulSoup(r.content, 'lxml')

        nameElement = soup.find('h1', class_='detailsInfo_right_title')
        for strong_tag in nameElement.find_all('strong'):
            strong_tag.decompose()
        name = nameElement.text.strip()

        try:
            rating = soup.find('div', class_='desc').text.strip()
        except:
            rating = 'No rating'

        try:
            stock = soup.find('span', class_='stockFlag').text.strip()
            stock = ''.join(filter(str.isdigit, stock))
            stockOutput = f"{stock} pzas."
        except:
            stockOutput = 'No stock'

        price = soup.find('span', class_='priceText').text.strip()

        data = {
            'Product': name,
            'Price': price,
            'Stock': stockOutput,
            'Rating': rating,
            'URL': link
        }

        dataList.append(data)
        print('Saving: ', data['Product'])

    return render_template('result.html', data=dataList)


@app.route('/download', methods=['POST'])
def download():
    global dataList
    # Convertir la lista de diccionarios en un DataFrame
    df = pd.DataFrame(dataList)
    # Escribir el DataFrame en un archivo Excel
    df.to_excel('servidores.xlsx', index=False)
    return send_file('servidores.xlsx', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)

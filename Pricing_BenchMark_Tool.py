import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

baseurl_1 = "https://www.cyberpuerta.mx/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

# Inicializar una lista para almacenar todos los enlaces
all_productlinks = []

# Variable para almacenar el máximo número de especificaciones encontrado
max_specifications = 0

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

    # Agregar los enlaces de la página actual a la lista de todos los enlaces
    all_productlinks.extend(productlinks)

    # Actualizar max_specifications si se encuentra un nuevo máximo
    for link in productlinks:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        characteristics = soup.find(
            'div', class_='detailsInfo_right_more_attribute').text.strip()
        characteristics = characteristics.replace(
            'Ver especificaciones completas', '').strip()
        # Split the characteristics into a list of individual items
        characteristics_list = [c.strip()
                                for c in characteristics.split('\n') if c.strip()]
        max_specifications = max(max_specifications, len(characteristics_list))

# Eliminar duplicados
all_productlinks = list(set(all_productlinks))

dataList = []
for link in all_productlinks:

    r = requests.get(link, headers=headers)

    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('h1', class_='detailsInfo_right_title').text.strip()

    try:
        stock = soup.find('span', class_='stockFlag').text.strip()
        stock = ''.join(filter(str.isdigit, stock))
        stockOutput = f"{stock} pzas."
    except:
        stockOutput = 'No stock'

    price = soup.find('span', class_='priceText').text.strip()

    characteristics = soup.find(
        'div', class_='detailsInfo_right_more_attribute').text.strip()
    characteristics = characteristics.replace(
        'Ver especificaciones completas', '').strip()

    # Split the characteristics into a list of individual items
    characteristics_list = [c.strip()
                            for c in characteristics.split('\n') if c.strip()]

    # Pad the characteristics list with empty strings to match the maximum number of specifications
    characteristics_list += [''] * \
        (max_specifications - len(characteristics_list))

    # Agregar el URL al diccionario
    data = {
        'Product': name,
        'Stock': stockOutput,
        'Specifications': "\n".join(characteristics_list),
        'Price': price,
        'URL': link  # Agregar el URL aquí
    }

    dataList.append(data)
    print('Saving: ', data['Product'])

# Convertir la lista de diccionarios en un DataFrame
df = pd.DataFrame(dataList)

# Escribir el DataFrame en un archivo CSV
df.to_csv('servidores.csv', index=False)

print('Datos guardados en servidores.csv exitosamente.')

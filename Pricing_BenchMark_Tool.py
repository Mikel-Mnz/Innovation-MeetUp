import requests
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

baseurl_1 = "https://www.cyberpuerta.mx/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

# Inicializar una lista para almacenar todos los enlaces
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

    # Agregar los enlaces de la página actual a la lista de todos los enlaces
    all_productlinks.extend(productlinks)

# Eliminar duplicados
all_productlinks = list(set(all_productlinks))

# testLink = 'https://www.cyberpuerta.mx/Computo-Hardware/Servidores/Servidores/Servidor-Lenovo-ThinkSystem-ST50-V2-3-2GHz-Intel-Xeon-E-2356G-16GB-DDR4-4TB-SATA-III-Torre-no-Sistema-Operativo-Instalado.html'

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
    # Busca la posición donde termina la parte de "Sistema operativo"
    end_index = characteristics.find(
        'Sistema operativo:') + len('Sistema operativo:')
    # Obtén la parte de la cadena antes de "Sistema operativo" y elimina espacios extra al final
    characteristics = characteristics[:end_index].strip()
    characteristics = characteristics.replace('\n', ' ')

    data = {
        'Product': name,
        'Stock': stockOutput,
        'Specifications': characteristics,
        'Price': price
    }

    print(data)

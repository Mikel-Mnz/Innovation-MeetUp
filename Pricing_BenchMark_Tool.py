import requests
from bs4 import BeautifulSoup

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

# Imprimir los enlaces filtrados
for link in all_productlinks:
    print(link)

print(len(all_productlinks))

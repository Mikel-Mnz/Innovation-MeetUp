# Definición de los productos como una lista de diccionarios
productos = [
    {"tipo": "laptop", "marca": "DELL", "modelo": "Laptop1", "especificaciones": "Especificaciones de Laptop1"},
    {"tipo": "laptop", "marca": "DELL", "modelo": "Laptop2", "especificaciones": "Especificaciones de Laptop2"},
    {"tipo": "laptop", "marca": "DELL", "modelo": "Laptop3", "especificaciones": "Especificaciones de Laptop3"},
    {"tipo": "laptop", "marca": "DELL", "modelo": "Laptop4", "especificaciones": "Especificaciones de Laptop4"},
    {"tipo": "laptop", "marca": "DELL", "modelo": "Laptop5", "especificaciones": "Especificaciones de Laptop5"},
    {"tipo": "laptop", "marca": "DELL", "modelo": "Macbook Pro", "especificaciones": "Especificaciones de Macbook Pro"},
    {"tipo": "base de datos", "marca": "DELL", "nombre": "MySQL", "version": "8.0", "especificaciones": "Especificaciones de MySQL 8.0"},
    {"tipo": "base de datos", "marca": "DELL", "nombre": "PostgreSQL", "version": "13", "especificaciones": "Especificaciones de PostgreSQL 13"},
    {"tipo": "base de datos", "marca": "DELL", "nombre": "SQL Server", "version": "2019", "especificaciones": "Especificaciones de SQL Server 2019"},
    {"tipo": "base de datos", "marca": "DELL", "nombre": "MongoDB", "version": "4.4", "especificaciones": "Especificaciones de MongoDB 4.4"},
    {"tipo": "base de datos", "marca": "DELL", "nombre": "Oracle", "version": "19c", "especificaciones": "Especificaciones de Oracle 19c"},
    {"tipo": "servidor", "marca": "DELL", "modelo": "ProLiant DL380 Gen10", "especificaciones": "Especificaciones de ProLiant DL380 Gen10"},
    {"tipo": "servidor", "marca": "DELL", "modelo": "ProLiant DL360 Gen10", "especificaciones": "Especificaciones de ProLiant DL360 Gen10"},
    {"tipo": "servidor", "marca": "DELL", "modelo": "ProLiant ML350 Gen10", "especificaciones": "Especificaciones de ProLiant ML350 Gen10"},
    {"tipo": "servidor", "marca": "DELL", "modelo": "ProLiant DL325 Gen10 Plus", "especificaciones": "Especificaciones de ProLiant DL325 Gen10 Plus"},
    {"tipo": "servidor", "marca": "DELL", "modelo": "ProLiant DL160 Gen10", "especificaciones": "Especificaciones de ProLiant DL160 Gen10"},

    {"tipo": "laptop", "marca": "HPE", "modelo": "Laptop1", "especificaciones": "Especificaciones de Laptop1"},
    {"tipo": "laptop", "marca": "HPE", "modelo": "Laptop2", "especificaciones": "Especificaciones de Laptop2"},
    {"tipo": "laptop", "marca": "HPE", "modelo": "Laptop3", "especificaciones": "Especificaciones de Laptop3"},
    {"tipo": "laptop", "marca": "HPE", "modelo": "Laptop4", "especificaciones": "Especificaciones de Laptop4"},
    {"tipo": "laptop", "marca": "HPE", "modelo": "Laptop5", "especificaciones": "Especificaciones de Laptop5"},
    {"tipo": "laptop", "marca": "HPE", "modelo": "Macbook Pro", "especificaciones": "Especificaciones de Macbook Pro"},
    {"tipo": "base de datos", "marca": "HPE", "nombre": "MySQL", "version": "8.0", "especificaciones": "Especificaciones de MySQL 8.0"},
    {"tipo": "base de datos", "marca": "HPE", "nombre": "PostgreSQL", "version": "13", "especificaciones": "Especificaciones de PostgreSQL 13"},
    {"tipo": "base de datos", "marca": "HPE", "nombre": "SQL Server", "version": "2019", "especificaciones": "Especificaciones de SQL Server 2019"},
    {"tipo": "base de datos", "marca": "HPE", "nombre": "MongoDB", "version": "4.4", "especificaciones": "Especificaciones de MongoDB 4.4"},
    {"tipo": "base de datos", "marca": "HPE", "nombre": "Oracle", "version": "19c", "especificaciones": "Especificaciones de Oracle 19c"},
    {"tipo": "servidor", "marca": "HPE", "modelo": "ProLiant DL380 Gen10", "especificaciones": "Especificaciones de ProLiant DL380 Gen10"},
    {"tipo": "servidor", "marca": "HPE", "modelo": "ProLiant DL360 Gen10", "especificaciones": "Especificaciones de ProLiant DL360 Gen10"},
    {"tipo": "servidor", "marca": "HPE", "modelo": "ProLiant ML350 Gen10", "especificaciones": "Especificaciones de ProLiant ML350 Gen10"},
    {"tipo": "servidor", "marca": "HPE", "modelo": "ProLiant DL325 Gen10 Plus", "especificaciones": "Especificaciones de ProLiant DL325 Gen10 Plus"},
    {"tipo": "servidor", "marca": "HPE", "modelo": "ProLiant DL160 Gen10", "especificaciones": "Especificaciones de ProLiant DL160 Gen10"},

    {"tipo": "laptop", "marca": "Oracle", "modelo": "Laptop1", "especificaciones": "Especificaciones de Laptop1"},
    {"tipo": "laptop", "marca": "Oracle", "modelo": "Laptop2", "especificaciones": "Especificaciones de Laptop2"},
    {"tipo": "laptop", "marca": "Oracle", "modelo": "Laptop3", "especificaciones": "Especificaciones de Laptop3"},
    {"tipo": "laptop", "marca": "Oracle", "modelo": "Laptop4", "especificaciones": "Especificaciones de Laptop4"},
    {"tipo": "laptop", "marca": "Oracle", "modelo": "Laptop5", "especificaciones": "Especificaciones de Laptop5"},
    {"tipo": "laptop", "marca": "Oracle", "modelo": "Macbook Pro", "especificaciones": "Especificaciones de Macbook Pro"},
    {"tipo": "base de datos", "marca": "Oracle", "nombre": "MySQL", "version": "8.0", "especificaciones": "Especificaciones de MySQL 8.0"},
    {"tipo": "base de datos", "marca": "Oracle", "nombre": "PostgreSQL", "version": "13", "especificaciones": "Especificaciones de PostgreSQL 13"},
    {"tipo": "base de datos", "marca": "Oracle", "nombre": "SQL Server", "version": "2019", "especificaciones": "Especificaciones de SQL Server 2019"},
    {"tipo": "base de datos", "marca": "Oracle", "nombre": "MongoDB", "version": "4.4", "especificaciones": "Especificaciones de MongoDB 4.4"},
    {"tipo": "base de datos", "marca": "Oracle", "nombre": "Oracle", "version": "19c", "especificaciones": "Especificaciones de Oracle 19c"},
    {"tipo": "servidor", "marca": "Oracle", "modelo": "ProLiant DL380 Gen10", "especificaciones": "Especificaciones de ProLiant DL380 Gen10"},
    {"tipo": "servidor", "marca": "Oracle", "modelo": "ProLiant DL360 Gen10", "especificaciones": "Especificaciones de ProLiant DL360 Gen10"},
    {"tipo": "servidor", "marca": "Oracle", "modelo": "ProLiant ML350 Gen10", "especificaciones": "Especificaciones de ProLiant ML350 Gen10"},
    {"tipo": "servidor", "marca": "Oracle", "modelo": "ProLiant DL325 Gen10 Plus", "especificaciones": "Especificaciones de ProLiant DL325 Gen10 Plus"},
    {"tipo": "servidor", "marca": "Oracle", "modelo": "ProLiant DL160 Gen10", "especificaciones": "Especificaciones de ProLiant DL160 Gen10"},

    {"tipo": "laptop", "marca": "Lenovo", "modelo": "Laptop1", "especificaciones": "Especificaciones de Laptop1"},
    {"tipo": "laptop", "marca": "Lenovo", "modelo": "Laptop2", "especificaciones": "Especificaciones de Laptop2"},
    {"tipo": "laptop", "marca": "Lenovo", "modelo": "Laptop3", "especificaciones": "Especificaciones de Laptop3"},
    {"tipo": "laptop", "marca": "Lenovo", "modelo": "Laptop4", "especificaciones": "Especificaciones de Laptop4"},
    {"tipo": "laptop", "marca": "Lenovo", "modelo": "Laptop5", "especificaciones": "Especificaciones de Laptop5"},
    {"tipo": "laptop", "marca": "Lenovo", "modelo": "Macbook Pro", "especificaciones": "Especificaciones de Macbook Pro"},
    {"tipo": "base de datos", "marca": "Lenovo", "nombre": "MySQL", "version": "8.0", "especificaciones": "Especificaciones de MySQL 8.0"},
    {"tipo": "base de datos", "marca": "Lenovo", "nombre": "PostgreSQL", "version": "13", "especificaciones": "Especificaciones de PostgreSQL 13"},
    {"tipo": "base de datos", "marca": "Lenovo", "nombre": "SQL Server", "version": "2019", "especificaciones": "Especificaciones de SQL Server 2019"},
    {"tipo": "base de datos", "marca": "Lenovo", "nombre": "MongoDB", "version": "4.4", "especificaciones": "Especificaciones de MongoDB 4.4"},
    {"tipo": "base de datos", "marca": "Lenovo", "nombre": "Oracle", "version": "19c", "especificaciones": "Especificaciones de Oracle 19c"},
    {"tipo": "servidor", "marca": "Lenovo", "modelo": "ProLiant DL380 Gen10", "especificaciones": "Especificaciones de ProLiant DL380 Gen10"},
    {"tipo": "servidor", "marca": "Lenovo", "modelo": "ProLiant DL360 Gen10", "especificaciones": "Especificaciones de ProLiant DL360 Gen10"},
    {"tipo": "servidor", "marca": "Lenovo", "modelo": "ProLiant ML350 Gen10", "especificaciones": "Especificaciones de ProLiant ML350 Gen10"},
    {"tipo": "servidor", "marca": "Lenovo", "modelo": "ProLiant DL325 Gen10 Plus", "especificaciones": "Especificaciones de ProLiant DL325 Gen10 Plus"},
    {"tipo": "servidor", "marca": "Lenovo", "modelo": "ProLiant DL160 Gen10", "especificaciones": "Especificaciones de ProLiant DL160 Gen10"},

    {"tipo": "laptop", "marca": "IBM", "modelo": "Laptop1", "especificaciones": "Especificaciones de Laptop1"},
    {"tipo": "laptop", "marca": "IBM", "modelo": "Laptop2", "especificaciones": "Especificaciones de Laptop2"},
    {"tipo": "laptop", "marca": "IBM", "modelo": "Laptop3", "especificaciones": "Especificaciones de Laptop3"},
    {"tipo": "laptop", "marca": "IBM", "modelo": "Laptop4", "especificaciones": "Especificaciones de Laptop4"},
    {"tipo": "laptop", "marca": "IBM", "modelo": "Laptop5", "especificaciones": "Especificaciones de Laptop5"},
    {"tipo": "laptop", "marca": "IBM", "modelo": "Macbook Pro", "especificaciones": "Especificaciones de Macbook Pro"},
    {"tipo": "base de datos", "marca": "IBM", "nombre": "MySQL", "version": "8.0", "especificaciones": "Especificaciones de MySQL 8.0"},
    {"tipo": "base de datos", "marca": "IBM", "nombre": "PostgreSQL", "version": "13", "especificaciones": "Especificaciones de PostgreSQL 13"},
    {"tipo": "base de datos", "marca": "IBM", "nombre": "SQL Server", "version": "2019", "especificaciones": "Especificaciones de SQL Server 2019"},
    {"tipo": "base de datos", "marca": "IBM", "nombre": "MongoDB", "version": "4.4", "especificaciones": "Especificaciones de MongoDB 4.4"},
    {"tipo": "base de datos", "marca": "IBM", "nombre": "Oracle", "version": "19c", "especificaciones": "Especificaciones de Oracle 19c"},
    {"tipo": "servidor", "marca": "IBM", "modelo": "ProLiant DL380 Gen10", "especificaciones": "Especificaciones de ProLiant DL380 Gen10"},
    {"tipo": "servidor", "marca": "IBM", "modelo": "ProLiant DL360 Gen10", "especificaciones": "Especificaciones de ProLiant DL360 Gen10"},
    {"tipo": "servidor", "marca": "IBM", "modelo": "ProLiant ML350 Gen10", "especificaciones": "Especificaciones de ProLiant ML350 Gen10"},
    {"tipo": "servidor", "marca": "IBM", "modelo": "ProLiant DL325 Gen10 Plus", "especificaciones": "Especificaciones de ProLiant DL325 Gen10 Plus"},
    {"tipo": "servidor", "marca": "IBM", "modelo": "ProLiant DL160 Gen10", "especificaciones": "Especificaciones de ProLiant DL160 Gen10"}
]


# Función para obtener la selección del usuario
def obtener_seleccion(productos):
    print("Seleccione dos productos para comparar:")
    for i, producto in enumerate(productos):
        if 'modelo' in producto:
            print(f"{i + 1}. {producto['marca']} - {producto['modelo']}")
        else:
            print(f"{i + 1}. {producto['marca']} - No hay modelo disponible")
    seleccion = []
    while len(seleccion) < 2:
        try:
            indice = int(input("Ingrese el número correspondiente al producto: ")) - 1
            if 0 <= indice < len(productos):
                seleccion.append(productos[indice])
            else:
                print("¡Índice fuera de rango! Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Ingrese un número.")
    return seleccion

# Función para comparar dos productos
def comparar_productos(producto1, producto2):
    print("Comparando productos:")
    print("Producto 1:", producto1)
    print("Producto 2:", producto2)
    # Aquí puedes agregar tu lógica de comparación

# Ejemplo de uso
if __name__ == "__main__":
    seleccion = obtener_seleccion(productos)
    comparar_productos(seleccion[0], seleccion[1])
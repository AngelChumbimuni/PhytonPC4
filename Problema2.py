import modulos.bd as bd
from modulos.proceso import *
from modulos.jobs import actualizar_tipo_cambio
from pyfiglet import Figlet
import random

database = None

def main():
    salir = False
    init = True
    while not salir:
        if init:
            user = input("Ingrese su nombre de usuario temporal: ")
            init = False
            config()

        opciones = """
        Bienvenidos a store DatuxTec
        1. Crear producto
        2. Listar productos
        3. Editar nombre de producto
        4. Eliminar producto
        5. Configuración inicial
        6. Usar pyfiglet para editar el título
        7. Actualizar tipo de cambio
        8. Editar precio o stock
        9. Buscar producto por nombre
        10. Agregar cliente
        11. Listar clientes
        12. Salir
        """

        print(opciones)
        opc = int(input("Ingrese una opción: "))

        if opc == 1:
            crear_producto(user)
        elif opc == 2:
            listar_producto(user)
        elif opc == 3:
            editar_nombre(user)
        elif opc == 4:
            eliminar_producto(user)
        elif opc == 5:
            config()
        elif opc == 6:
            usar_pyfiglet()
        elif opc == 7:
            actualizar_tipo_cambio()
        elif opc == 8:
            editar_precio_stock(user)
        elif opc == 9:
            buscar_producto_por_nombre()
        elif opc == 10:
            agregar_cliente()
        elif opc == 11:
            listar_clientes()
        elif opc == 12:
            salir = True
            print("Terminando sesión....")
            break
        else:
            print("Ingrese una opción válida")

def config():
    global database
    database = bd.Bd()

    query_products = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        );
    """

    query_tipo_cambio = """
        CREATE TABLE IF NOT EXISTS tipo_cambio (
            id INTEGER PRIMARY KEY,
            valor REAL NOT NULL,
            fecha DATE NOT NULL
        );
    """

    query_cliente = """
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            direccion VARCHAR(200) NOT NULL,
            telefono VARCHAR(15) NOT NULL
        );
    """

    database.execute_query(query_products)
    database.execute_query(query_tipo_cambio)
    database.execute_query(query_cliente)

def usar_pyfiglet():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    fuente_seleccionada = random.choice(fuentes_disponibles)
    
    texto_imprimir = input("Ingrese el texto para imprimir: ")
    
    figlet.setFont(font=fuente_seleccionada)
    print(figlet.renderText(texto_imprimir))

if __name__ == '__main__':
    main()
"crear un nuevo archivo llamado jobs.py en la carpeta modulos con el siguiente contenido:"
import requests
from modulos.bd import Bd

def actualizar_tipo_cambio():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)
    data = response.json()

    if data.get('valor') is not None and data.get('fecha') is not None:
        database = Bd()
        query = f"INSERT INTO tipo_cambio (valor, fecha) VALUES ({data['valor']}, '{data['fecha']}');"
        database.execute_query(query)
        print("Tipo de cambio actualizado correctamente.")
    else:
        print("No se pudo obtener la información del tipo de cambio.")

def editar_precio_stock(user):
    # Implementa la lógica para editar precio o stock
    pass

def buscar_producto_por_nombre():
    # Implementa la lógica para buscar producto por nombre
    pass

def agregar_cliente():
    # Implementa la lógica para agregar un cliente
    pass

def listar_clientes():
    # Implementa la lógica para listar clientes
    pass

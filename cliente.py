import sys
import logging
import threading
import time

from signalrcore.hub_connection_builder import HubConnectionBuilder



# Variables
server_url = "wss://socket-iac.azurewebsites.net/pruebas"

detener = False

def worker():
    arreglo = [1,2,3,4,5]
    
    for item in arreglo:
        time.sleep(0.5)
        hub_connection.send("RecibirMediciones", ['{ "name":"John", "age":30, "city":"New York"}'])

        

def start():
    t = threading.Thread(target=worker)
    t.start()




hub_connection = HubConnectionBuilder()\
    .with_url(server_url)\
    .build()

hub_connection.on_open(lambda: print("Conexion Establecida"))
hub_connection.on_close(lambda: print("connection closed"))


# Escuchar eventos del servidor
hub_connection.on("Iniciar", lambda callback_function : start())
hub_connection.on("Pausar", lambda callback_function : stop())


# Iniciar conexion con el servidor
hub_connection.start()





while True:
    continue


hub_connection.stop()

sys.exit(0)
import sys
import logging

from signalrcore.hub_connection_builder import HubConnectionBuilder

from interval import *


# Variables
server_url = "wss://socket-iac.azurewebsites.net/pruebas"


def action():
    hub_connection.send("RecibirMediciones", ['{ "name":"John", "age":30, "city":"New York"}'])



def start():
    inter = setInterval(0.5, action)
    t = threading.Timer(30, inter.cancel)
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
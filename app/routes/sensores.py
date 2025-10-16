from Adafruit_IO import Client, Feed, Data, RequestError, MQTTClient
import time
#MQTTCLiente protocolo de mensajeria

aio = Client(AIO_USERNAME, AIO_KEY)

TEMPERATURA_FEED = "temperatura"
HUMEDAD_FEED = "humedad"
LUZ_FEED = "luz"
FEEDS = ["temperatura", "humedad", "luz"]

valores = {"temperatura": None, "humedad": None, "luz": None}


#aqui colocamos cuando la conexion es exitosa
def connected(client):
    print("Conectado a Adafruit IO!")
    for feed in FEEDS:
        #para indicar cuales feeds queremos escuchar
        client.subscribe(feed)
        print(f"Suscrito al feed: {feed}")

#al tener suscripciones se ejecuta cada vez que recibe un dato
def message(client, feed_id, payload):
    valores[feed_id] = payload
    print(f"Nuevo mensaje en {feed_id}: {payload}")

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_message = message



client.connect()

client.loop_background()

def obtener_datos():
    return valores


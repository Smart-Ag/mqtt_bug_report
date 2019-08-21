import paho.mqtt.client as mqtt
import json
import time

def utf8len(s):
    return len(s.encode('utf-8'))

client = mqtt.Client()

print('client is', client)
client.loop_start()
client.connect_async('127.0.0.1', port=1883, keepalive=60)

cache = '0' * (1024**2)

print("size of string: ", str(utf8len(cache)))

while True:
    cov_cmd = {"data": cache,"timestamp":time.time() * 1000}
    to_send = json.dumps(cov_cmd).encode('ascii')
    client.publish('mqtt/demo', to_send)
    print("sent: ", str(time.time()))
    time.sleep(5)
import paho.mqtt.client as mqtt
import json
import time

def utf8len(s):
    return len(s.encode('utf-8'))

def got_msg(client, userdata, msg):
    json_msg = json.loads(msg.payload.decode('ascii'))

    print("Recieved msg in: ", (time.time() * 1000) - json_msg['timestamp'], ' ms.')

client = mqtt.Client()
print('client is', client)
client.on_message = got_msg
client.connect('127.0.0.1', port=1883, keepalive=60)
client.loop_start()

cache = '0' * (1024**2)

print("size of string: ", str(utf8len(cache)))

client.subscribe('mqtt/demo')

while True:
    cov_cmd = {"data": cache,"timestamp":time.time() * 1000}
    to_send = json.dumps(cov_cmd).encode('ascii')
    client.publish('mqtt/demo', to_send)
    print("sent: ", str(time.time()))
    time.sleep(5)
from micropyserver import MicroPyServer
import esp
import network
import config
import time
import utils
import json
import http_client
url = "https://53e6d1a2-e1b5-4d74-bcce-42450a1544b7.mock.pstmn.io/addrecord"

print(config.wifi_name, config.wifi_pass)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print('wifi starting...')
if wlan.isconnected() == False:
    wlan.connect(config.wifi_name, config.wifi_pass)
    while wlan.isconnected() == False:
        time.sleep(1)
print('Device IP:', wlan.ifconfig()[0])

def show_message(request):
    ''' request handler '''
    server.send("HELLO WORLD!")
    r = http_client.post(url, json ={"hello": "world"})
    print(r.content)

server = MicroPyServer()
server.add_route("/", show_message)
server.start()



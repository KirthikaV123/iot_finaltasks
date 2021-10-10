import network
from time import sleep
wlan = network.WLAN(network.sta_if)
if not wlan.isconnected():
    wlan.active(True)
    print('Trying to connect')
    wlan.connect('The Amazing Wifi', '12345678') # Connect to an AP
    while not wlan.isconnected():
        pass
print("network configuration",wlan.ifconfig())   




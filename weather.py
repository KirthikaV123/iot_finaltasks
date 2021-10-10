import network
import socket
import urequests
import ujson as json

#wificonnection
def connect_Wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network')
        wlan.connect('The Amazing Wifi', '12345678') # Replacing with wifi credentials
        while not wlan.isconnected():
            pass
    display.text('Connected', 0, 20) # Print connected once connected 
    display.show()
def weather_data():
    weatherurl="http://dataservice.accuweather.com/forecasts/v1/daily/1day/206671?apikey=Y89KvqQD9p7lP5cBuSURERSqbSyObcAT&details=true"
    data = weatherurl.json()
    return data

def print_climate_data(data):

        place = data["title"]
        #Get Todays Data First
        weather = data["consolidated_weather"]
        date_entered = weather["date"]
        weather_obtained = weather["weather_state"]
        temperature = weather["temp"]
        Humidity = weather["humidity"]
        
        print(place)
        print(date_entered)
        print(weather_obtained)
        print(temperature)

connect_Wifi() # Connecting to the network
 
while True:
    data=get_data()  # obtaining weather data in json format


        
        
        
        
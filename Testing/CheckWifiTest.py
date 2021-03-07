import requests

def checkWifi():
    try:
        r = requests.get("http://www.google.com",
                         timeout=20)  # Send request to google, it will timeout with exception if it fails
        return True  # We are connected to wifi
    except:
        return False  # We are not connected to wifi


checkWifi() #Repeat this when the
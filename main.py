# discord: maxxusx
# twitter:  ̶M̶a̶x̶x̶u̶s̶Y̶T̶  got sussed by furry. new acc: MaxxusYT2

print("discord: maxxusx")
print("twitter: MaxxusYT2")

##########################################################################################################################

import requests
import pyfiglet

##########################################################################################################################

banner = pyfiglet.figlet_format("maxxusx")
print(banner)

webhook = input("webhook url: ")

msg = input("message: ")

##########################################################################################################################

def send(msg, webhook):
        data = requests.post(webhook, json={'content': msg})
        exit()
        
send(msg, webhook)
import os
import requests
import random
from colorama import Fore, Style, init
import time
import json
from os import system, write
import warnings
import re
import twocaptcha
from twocaptcha import TwoCaptcha
import threading
import webbrowser
from pynput.keyboard import Key, Controller
warnings.filterwarnings("ignore")
import pyautogui

keyboard = Controller()
special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

os.system("title NationGenerator")




init(convert=True)

def banner():
    print(f"""{Fore.LIGHTBLUE_EX}
                                       ╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
                                       ║║║╠═╣ ║ ║║ ║║║║  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
                                       ╝╚╝╩ ╩ ╩ ╩╚═╝╝╚╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═
    
    """)

banner()



def inputs():
 print("")
print("The generator will not work if : ")
print()
print("1)If you insert an invalid key")
print("2)If you insert a key with 0 balance")
print()
captchakey = input("Your 2captcha key : ")
os.system('cls')
banner()
username = input("Insert the username to use (more than 2 characters): ")
n = len(username)
if(special_char.search(username) == None):
    pass
else:
    print("")
    print(f"{Fore.RED}Please do not use special characters!")
    time.sleep(2)
    os.close()
if n == 1:
 print("")
 print(f"{Fore.RED}The name must have 2 or more characters!")
 time.sleep(2)
 os.close()
else:
    os.system('cls')
    banner()
    pass
    

password = input("Insert the password to use (more than 6 characters): ")
n = len(password)
if n == 1:
    print(f"{Fore.RED}The password must have 6 or more characters!")
    time.sleep(2)
    os.close()

elif n == 2:
    print("")
    print(f"{Fore.RED}The password must have 6 or more characters!")
    time.sleep(2)
    os.close()

elif n == 3:
    print("")
    print(f"{Fore.RED}The password must have 6 or more characters!")
    time.sleep(2)
    os.close()

elif n == 4:
    print("")
    print(f"{Fore.RED}The password must have 6 or more characters!")
    time.sleep(2)
    os.close()

elif n == 5:
    print("")
    print(f"{Fore.RED}The password must have 6 or more characters!")
    time.sleep(2)
    os.close()

else :
    pass

inputs()
os.system('cls')
banner()

proxy = set()

with open("Proxies.txt", "r") as f:
        file_lines1 = f.readlines()
        for line1 in file_lines1:
            proxy.add(line1.strip())
            

proxiesRandom = {
        'https': 'http://'+random.choice(list(proxy))}
print(proxiesRandom)

randemail = lines = open("Emails.txt").readlines() 
line = lines[0] 
email = line.split() 
emailpicked = random.choice(email)

response = requests.get("https://discord.com/register")
if response.status_code == 200:
    time.sleep(2)
    print ('Successfully started the registration...')

    

else:
    print ('ERROR! cant start the registration.')
    time.sleep(2)
    os.close()



payload = {

"fingerprint": "880846299564474429.NgzXoHICT-ChBgtN4mY0g7imRWk", 
"email": emailpicked,
"captcha_key": captchakey,
"consent": True,
"date_of_birth": "1980-05-04",
"email": emailpicked,
"fingerprint": "880846299564474429.NgzXoHICT-ChBgtN4mY0g7imRWk",
"gift_code_sku_id": None,
"invite": None,
"password": password,
"username": username,
}

print (payload)
header = {
"authority": "discord.com",
"method" : "POST",
"path": "/api/v9/auth/register",
"scheme": "https",
"accept": "*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "it",
"content-length": "263",
"content-type": "application/json",
"cookie": "__dcfduid=3fd903fecb65d7f52a108e9f69ce4d95; __stripe_mid=1178c7ce-fe79-4d91-8bde-693ec5aad9e2b829a2; _ga=GA1.2.2094573270.1625836775; __sdcfduid=148b1db0f42911ebb8f70d3c76bddaf4f9f1bedd54b786ac29a5619a22850e1ef5c35bc5c992c25d2a192ebc77e42deb; OptanonConsent=isIABGlobal=false&datestamp=Thu+Aug+26+2021+13%3A00%3A58+GMT%2B0200+(Ora+legale+dell%E2%80%99Europa+centrale)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0&AwaitingReconsent=false; __cfruid=b901b8d782b69ff472e986f3116af40248e03e3d-1630149980",
"origin": "https://discord.com",
"referer": "https://discord.com/register?email=b0s.h.eon.tr.acke%40gmail.com&redirect_to=%2Fchannels%2F%40me",
"sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
"sec-ch-ua-mobile": "?1",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
"x-debug-options": "bugReporterEnabled",
"x-fingerprint": "880846299564474429.NgzXoHICT-ChBgtN4mY0g7imRWk",
"x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6Iml0LUlUIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xNTkgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjkyLjAuNDUxNS4xNTkiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTUzNTEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
}

i = 0

while i > 1:
    print()
resp = requests.post('https://discord.com/api/v9/auth/register', proxies=None, headers=header, data=json.dumps(payload))
if resp.status_code == 200 :
    token = response.json()
    data = token['token']
    print("Token successfully created : " + token)
    with open(f"Tokens.txt", "a+") as f:
                f.write(str(data + '\n'))
                f.close()
    print("Verifying the email...")
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open("https://accounts.google.com/AddSession/identifier?hl=it&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'a')
    keyboard.type('seniorriccardomilos@gmail.com')
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type('3711981601aS..')
    keyboard.press(Key.enter)
    print("successfully verified!")
    os.system("taskkill /im chrome.exe /f")
    time.sleep(2)
    
else :
    print("some error occurred")

time.sleep(2)

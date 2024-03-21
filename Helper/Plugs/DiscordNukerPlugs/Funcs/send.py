import threading
import requests
import time
import sys
import ctypes
import os
from colorama import Fore, Style
count2 = 0

Channel_delted2 = sys.argv[1]
Channel_created = sys.argv[2]
count = sys.argv[3]
message = sys.argv[4]

def set_window_title(title):
    try:
        console_handle = ctypes.windll.kernel32.GetConsoleWindow()

        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except Exception as e:
        print(f'Error occurred while setting window title: {str(e)}')

def upodate_title():
    set_window_title(f"Nexus Nuker Channels Delted: {Channel_delted2} | Channels Created: {Channel_created} | Webhooks Created: {count} | Messages Send: {count2} | Spamming Message: {message} ")

class Log:
    @staticmethod
    def err(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTRED_EX} ERROR {Fore.RESET}] {msg}')

    @staticmethod
    def succ(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTMAGENTA_EX}+{Fore.RESET}] {msg}')

    @staticmethod
    def console(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTMAGENTA_EX}-{Fore.RESET}] {msg}')

    @staticmethod
    def invalid(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTMAGENTA_EX} INVALID {Fore.RESET}] {msg}')
        #

def send_message(webhook_url, message):
    global count2
    payload = {'content': message}
    payload["avatar_url"] = "https://cdn.discordapp.com/attachments/1138264267058065420/1157398437998886973/RmDJt7xVhNFTA6yvy3EWfsTbki45EeI67K93h75F_1.png?ex=651876cb&is=6517254b&hm=885b1abcbdbf40a1754ccddace833bde387a83ff14b0b1b15282d93da965fe5a&"
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(webhook_url, json=payload, headers=headers)
        if response.status_code == 204:
            count2 += 1
            upodate_title()
        else:
            print(f"Failed to send message to {webhook_url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending message to {webhook_url}: {str(e)}")

webhook_file = 'Output/Nuker/webhooks.txt'

while True:
    with open(webhook_file, 'r') as file:
        webhook_urls = file.readlines()

    message_to_send = message

    threads = []

    for url in webhook_urls:
        url = url.strip() 
        thread = threading.Thread(target=send_message, args=(url, message_to_send))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

    os.system("cls")
    Log.succ(f'Deleted channel' + Fore.MAGENTA + f" {(Channel_delted2)}" + Fore.RESET)
    Log.succ(f"Channel created" + Fore.MAGENTA + f" {(Channel_created)}" + Fore.RESET )
    Log.succ(f'Webhooks Created' + Fore.MAGENTA + f" {(count)}" + Fore.RESET)
    Log.succ(f'Messages Send' + Fore.MAGENTA + f" {(count2)}" + Fore.RESET)
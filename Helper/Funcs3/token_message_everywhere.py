from Helper import *
from Helper.Common.utils import *

async def send_message_to_channel(session, token, guild_id, channel_id, message):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data = {
        'content': message
    }
    async with session.post(url, headers=headers, json=data) as response:
        if response.status == 200:
            print(f"{lc} Message sent to channel {channel_id} in guild {guild_id}.")

async def send_messages_to_channels(token, message):
    url = 'https://discord.com/api/v9/users/@me/guilds'
    headers = {
        'Authorization': token
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                print("Failed to fetch guilds. Make sure the token is correct.")
                return
            guilds = await response.json()
            tasks = []
            for guild in guilds:
                guild_id = guild['id']
                async with session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers) as channels_response:
                    if channels_response.status != 200:
                        continue
                    channels = await channels_response.json()
                    for channel in channels:
                        channel_id = channel['id']
                        channel_type = channel['type']
                        if channel_type != 0: 
                            continue
                        task = send_message_to_channel(session, token, guild_id, channel_id, message)
                        tasks.append(task)
                        if len(tasks) >= 15:
                            await asyncio.gather(*tasks)
                            tasks = []
            if tasks:  
                await asyncio.gather(*tasks)


def meessage_everywhere_spam():
    new_title("Discord Message Everywhere discord.gg/nexustools")
    token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
    message = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Message: ")
    asyncio.run(send_messages_to_channels(token, message))
    input("Press Enter To continue...")

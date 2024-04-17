from Helper import *
from Helper.Common.utils import *


def fetch_user_details():
    new_title("Token info discord.gg/nexustools")
    token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
    headers = {
        'Authorization': token
    }

    user_response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)

    if user_response.status_code != 200:
        print(Fore.RED + "Failed to fetch user details. Make sure the token is correct." + Style.RESET_ALL)
        return

    user_data = user_response.json()


    created_at = datetime.utcfromtimestamp(((int(user_data['id']) >> 22) + 1420070400000) / 1000)

    print(Fore.GREEN + "User Details:" + Style.RESET_ALL)
    print(f"{Fore.CYAN}Token:{Style.RESET_ALL} {token}")
    print(f"{Fore.CYAN}ID:{Style.RESET_ALL} {user_data['id']}")
    print(f"{Fore.CYAN}Username:{Style.RESET_ALL} {user_data['username']}")
    print(f"{Fore.CYAN}Discriminator:{Style.RESET_ALL} {user_data['discriminator']}")
    print(f"{Fore.CYAN}Avatar URL:{Style.RESET_ALL} https://cdn.discordapp.com/avatars/{user_data['id']}/{user_data['avatar']}.png")
    print(f"{Fore.CYAN}Locale:{Style.RESET_ALL} {user_data['locale']}")
    print(f"{Fore.CYAN}Email:{Style.RESET_ALL} {user_data.get('email', 'Not available')}")
    print(f"{Fore.CYAN}Phone:{Style.RESET_ALL} {user_data.get('phone', 'Not available')}")
    print(f"{Fore.CYAN}Account Creation Date:{Style.RESET_ALL} {created_at}")


    connections_response = requests.get('https://discord.com/api/v9/users/@me/connections', headers=headers)

    if connections_response.status_code == 200:
        connections_data = connections_response.json()
        if connections_data:
            print("\nConnected Accounts:")
            for connection in connections_data:
                print(f"{Fore.CYAN}Type:{Style.RESET_ALL} {connection['type']}")
                print(f"{Fore.CYAN}Name:{Style.RESET_ALL} {connection['name']}")
                print(f"{Fore.CYAN}ID:{Style.RESET_ALL} {connection['id']}\n")
        else:
            print("No connected accounts.")
    else:
        print("Failed to fetch connected accounts.")


    guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)

    if guilds_response.status_code == 200:
        guilds_data = guilds_response.json()
        guild_count = len(guilds_data)
        owner_guilds = [guild for guild in guilds_data if guild['owner']]
        owner_guild_count = len(owner_guilds)
        print(f"{Fore.GREEN}\nGuild Count:{Style.RESET_ALL} {guild_count}")
        print(f"{Fore.GREEN}Owner Guild Count:{Style.RESET_ALL} {owner_guild_count}")
        if owner_guilds:
            print("\nOwner Guilds:")
            for guild in owner_guilds:
                print(f"{Fore.CYAN}Name:{Style.RESET_ALL} {guild['name']} {Fore.CYAN}(ID:{Style.RESET_ALL} {guild['id']})")
    else:
        print("Failed to fetch guilds.")

    input("Press Enter To continue...")

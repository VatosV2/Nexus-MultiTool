from Helper import *
from Helper.Common.utils import *


def count_guilds(token, printt):
    if printt == "full":
        token_display = token
    elif printt == "partial":
        token_display = token[:20]
    else:
        print("Invalid choice for token display. Defaulting to full token.")
        token_display = token

    headers = {
        'Authorization': token
    }

    response = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)

    if response.status_code == 200:
        guilds = response.json()
        guild_count = len(guilds)

        if printt == "full":
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token_display}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}{guild_count} GUILDS{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        else:
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token_display}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}{guild_count} GUILDS{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        if printt == "full":
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token_display}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}FAILED FETCH GUILDS{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.LIGHTBLACK_EX}({response.status_code})")
        else:
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token_display}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}FAILED FETCH GUILDS{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.LIGHTBLACK_EX}({response.status_code})")


def guild_count():
    new_title("Token Guild count checker discord.gg/nexustools")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Hide Tokens? (y/n): ")
    if choice == "y":
        printt = "partial"
    elif choice == "n":
        printt = "full"
    else:
        printt = "full"
        print("Invalid choice. Displaying full tokens by default.")
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    threads = []
    for token in tokens:
        token = token.strip()
        thread = threading.Thread(target=count_guilds, args=(token, printt))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    input("Press Enter To continue...")



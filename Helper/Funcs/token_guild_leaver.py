from Helper import *
from Helper.Common.utils import *



left = 0
not_inside = 0
inv = 0

def leave_server(guild_id, token, count_lock):
    global left, not_inside, inv
    headers = {
        "Authorization": token,
    }

    response = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers=headers)

    if response.status_code == 204:
        with count_lock:
            left += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Left Server: [{Fore.BLUE}{guild_id}{Fore.RESET}]')
    if response.status_code == 401 or 404:
        with count_lock:
            not_inside += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Isn\'t in the Guild id: [{Fore.BLUE}{guild_id}{Fore.RESET}]')
    else:
        with count_lock:
            inv += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Is Invalid or couldn\'t be checked')

def token_leave_server():
    new_title("Nexus Token Leaver")
    tokens = get_tokens()
    guild_id = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Input Server ID to leave: ")

    count_lock = threading.Lock()
    global left, not_inside, inv


    threads = []
    for token in tokens:
        token = token.strip()
        thread = threading.Thread(target=leave_server, args=(guild_id, token, count_lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"{ld} {Fore.GREEN}{left}{Fore.RESET} Tokens Left the server")
    print(f"{ld} {Fore.GREEN}{not_inside}{Fore.RESET} Tokens Wasnt in the server")
    print(f'{ld} {Fore.GREEN}{inv}{Fore.RESET} Invalid Tokens')
    input("Press Enter To continue...")


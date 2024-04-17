from Helper import *
from Helper.Common.utils import *

in_guild = 0
not_guild = 0
invalid = 0
in_guild_list = []


def check_token_gid(token, guild_id):
    global in_guild, not_guild, invalid
    headers = {
        'Authorization': token.strip()
    }
    response = requests.get(f'https://discord.com/api/v10/guilds/{guild_id}', headers=headers)
    if response.status_code == 200:
        in_guild += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} is in the Guild id: [{Fore.BLUE}{guild_id}{Fore.RESET}]')
        with open(f'Output/ServerIdChecker/{guild_id}_tokens.txt', 'a') as output_file:
            output_file.write(f'{token.strip()}\n')
    elif response.status_code == 401 or 404:
        not_guild += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Isn\'t in the Guild id: [{Fore.BLUE}{guild_id}{Fore.RESET}]')
    
    else:
        invalid += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Is Invalid or couldn\'t be checked')

def check_tokens_guild():
    new_title("Token Guild Checker discord.gg/nexustools")
    global in_guild, not_guild, invalid
    new_title("Nexus Token Guild Checker")
    tokens = get_tokens()
    guild_id = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Guild id: ")
    with open(f'Output/ServerIdChecker/{guild_id}_tokens.txt', 'w') as File:
        File.close()
    threads = []
    for token in tokens:
        thread = threading.Thread(target=check_token_gid, args=(token, guild_id))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        
    print(f"{ld} Tokens In Guild: {Fore.GREEN}{in_guild}{Fore.RESET}")
    print(f"{ld} Token Not in Guild: {Fore.GREEN}{not_guild}{Fore.RESET}")
    print(f"{ld} Invalid tokens: {Fore.GREEN}{invalid}{Fore.RESET}")
    print(f"{ld} Total tokens: {Fore.GREEN}{in_guild + not_guild + invalid}{Fore.RESET}")
    input("Press Enter To continue...")
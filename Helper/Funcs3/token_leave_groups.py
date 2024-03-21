from Helper import *
from Helper.Common.utils import *

def leave_all_group_chats(token):
    headers = {
        'Authorization': token
    }
    
    response = requests.get('https://discord.com/api/v9/users/@me/channels', headers=headers)
    
    if response.status_code == 200:
        channels = response.json()
        for channel in channels:
            if channel['type'] == 3:  
                channel_id = channel['id']
                response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers)
                if response.status_code == 200:
                    print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}LEFT{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
                else:
                    print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}FAILED TO LEAVE{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.LIGHTBLACK_EX}({response.status_code})')
    else:
        print(f'{Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}FAILED TO LEAVE{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')


def leave_groups():
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    threads = []
    for token in tokens:
        token = token.strip()
        thread = threading.Thread(target=leave_all_group_chats, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    input("Press Enter To continue...")
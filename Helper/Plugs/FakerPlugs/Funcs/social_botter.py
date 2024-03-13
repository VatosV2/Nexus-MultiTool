from Helper import *
from Helper.Common.utils import *


def get_random_count(typ):
    if typ == "views":
        return random.randint(250, 2000)
    elif typ == "likes":
        return random.randint(25, 150)
    elif typ == "shares":
        return random.randint(10, 70)
    elif typ == "follower":
        return random.randint(100, 700)
    else:
        return 0

def fake_social_bot():
    typ_list = ["Likes", "Views", "Shares", "Follower"]
    service = ""
    while service not in ["tiktok", "youtube"]:
        service = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] What Service? (tiktok, youtube): ").lower()
        if service not in ["tiktok", "youtube"]:
            print("Invalid Service")
    typ = ""
    while typ.capitalize() not in typ_list:
        typ = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] What Type? (Likes, Views, Shares, Follower): ").capitalize()
        if typ.capitalize() not in typ_list:
            print("Invalid Type")
    url = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] URL: ")
    while True:
        random_count = get_random_count(typ.lower())
        print(f"{lc} {Fore.BLUE}Url={Fore.WHITE}{url}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ADDED {random_count} {typ}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        time.sleep(1)



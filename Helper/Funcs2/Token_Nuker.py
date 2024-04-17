from Helper import *
from Helper.Common.utils import *
from Helper.Plugs.TokenNukerPlugs import *

def Token_nuker():
    new_title("Token Nuker discord.gg/nexustools")
    clear()
    print(banner)
    print(f"{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}] Nuke Token")
    print(f"[{Fore.MAGENTA}2{Fore.RESET}] Leave Servers")
    print(f"[{Fore.MAGENTA}3{Fore.RESET}] Delete Friends")
    print(f"[{Fore.MAGENTA}4{Fore.RESET}] Delete Servers")
    print(f"[{Fore.MAGENTA}5{Fore.RESET}] Mass Dm")
    print(f"[{Fore.MAGENTA}6{Fore.RESET}] Close Dms")
    print(f"[{Fore.MAGENTA}7{Fore.RESET}] Block All Friends")
    print(f"[{Fore.MAGENTA}8{Fore.RESET}] Fuck account")
    print(f"[{Fore.MAGENTA}0{Fore.RESET}] Leave")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    if choice == "1":
        clear()
        print(banner)
        token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
        Nuke_account(token)
        Token_nuker()
    elif choice == "2":
        clear()
        print(banner)
        token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
        leaveServer(token)
        Token_nuker()
    elif choice == "3":
        clear()
        print(banner)
        token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
        deleteFriends(token)
        Token_nuker()
    elif choice == "4":
        clear()
        print(banner)
        token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
        deleteServers(token)
        Token_nuker()
    elif choice == "5":
        clear()
        print(banner)
        token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
        content = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Message: ")
        massDM(token, content)
        Token_nuker()
    elif choice == "6":
        clear()
        print(banner)
        token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
        close_all_dms(token)
        Token_nuker()
    elif choice == "7":
        clear()
        print(banner)
        token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
        blockAllFriends(token)
        Token_nuker()
    elif choice == "8":
        clear()
        print(banner)
        token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
        fuckAccount(token)
        Token_nuker()
    elif choice == "0":
        quit1()
    else:
        print("invalid")
        time.sleep(1)
        Token_nuker()
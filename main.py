from Helper import *
from Helper.Common.utils import *

clear()

def main():
    new_title("Nexus MultiTool")
    clear()
    print(banner)
    print("                               ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}1{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Formater{Fore.LIGHTMAGENTA_EX}]", "    ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}8{Fore.LIGHTMAGENTA_EX}>>  [{Fore.RESET}Proxy Scraper{Fore.LIGHTMAGENTA_EX}]" )
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}2{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Checker{Fore.LIGHTMAGENTA_EX}]", "     ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}9{Fore.LIGHTMAGENTA_EX}>>  [{Fore.RESET}Proxy Checker{Fore.LIGHTMAGENTA_EX}]" )
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}3{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Sorter{Fore.LIGHTMAGENTA_EX}]", "      ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}10{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Obfuscate File{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}4{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Remove Doubles{Fore.LIGHTMAGENTA_EX}]", "    ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}11{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Tool{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}5{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Guild Checker{Fore.LIGHTMAGENTA_EX}]", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}12{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Faker Tool{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}6{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Guild Leaver{Fore.LIGHTMAGENTA_EX}]",  "", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}13{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Clear output Folder{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}7{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Spammer{Fore.LIGHTMAGENTA_EX}]", "     ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}14{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Nexus Discord{Fore.LIGHTMAGENTA_EX}]")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    if choice == "1":
        clear()
        print(banner)
        formater()
    elif choice == "2":
        clear()
        print(banner)
        Token_checker()
    elif choice == "3":
        clear()
        print(banner)
        sort_tokens()
    elif choice == "4":
        clear()
        print(banner)
        remove_duplicates()
    elif choice == "5":
        clear()
        print(banner)
        check_tokens_guild()
    elif choice == "6":
        clear()
        print(banner)
        token_leave_server()
    elif choice == "7":
        clear()
        print(banner)
        token_spammer()
    elif choice == "8":
        clear()
        print(banner)
        Proxy_scraper()
    elif choice == "9":
        clear()
        print(banner)
        check_proxys()    
    elif choice == "10":
        clear()
        print(banner)
        obfuscate()
    elif choice == "11":
        Webhook_tool()       
    elif choice == "12":
        main_faker()
    elif choice == "13":
        clear()
        print(banner)
        clear_output()
    elif choice == "14":
        discord()
    else:
        print("invalid chocie")
        time.sleep(1)
    main()

StartupTool()
main()
from Helper import *
from Helper.Common.utils import *

clear()

def main():
    new_title("Nexus MultiTool │ Page 1")
    clear()
    print(banner)
    print("                               ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}1{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Formater{Fore.LIGHTMAGENTA_EX}]", "    ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}8{Fore.LIGHTMAGENTA_EX}>>  [{Fore.RESET}Proxy Scraper{Fore.LIGHTMAGENTA_EX}]" )
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}2{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Checker{Fore.LIGHTMAGENTA_EX}]", "     ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}9{Fore.LIGHTMAGENTA_EX}>>  [{Fore.RESET}Proxy Checker{Fore.LIGHTMAGENTA_EX}]" )
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}3{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Sorter{Fore.LIGHTMAGENTA_EX}]", "      ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}10{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Obfuscate File{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}4{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Remove Doubles{Fore.LIGHTMAGENTA_EX}]", "    ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}11{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Tool{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}5{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Guild Checker{Fore.LIGHTMAGENTA_EX}]", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}12{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Faker Tool{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}6{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Guild Leaver{Fore.LIGHTMAGENTA_EX}]",  "", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}13{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Clear output Folder{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}7{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Spammer{Fore.LIGHTMAGENTA_EX}]", "     ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}14{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Next Page{Fore.LIGHTMAGENTA_EX}]")
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
        main2()
    else:
        print("invalid chocie")
        time.sleep(1)
    main()

def main2():
    new_title("Nexus MultiTool │ Page 2")
    clear()
    print(banner)
    print("                               ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}15{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Mail verifier{Fore.LIGHTMAGENTA_EX}]", "    ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}22{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Discord Nuker{Fore.LIGHTMAGENTA_EX}]" )
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}16{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Pass Changer{Fore.LIGHTMAGENTA_EX}]", "     ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}23{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Get Own Token{Fore.LIGHTMAGENTA_EX}]" )
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}17{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Onliner{Fore.LIGHTMAGENTA_EX}]", "          ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}24{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Login{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}18{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Status Rotater{Fore.LIGHTMAGENTA_EX}]", "   ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}25{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Pc CLeaner{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}19{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Nuker{Fore.LIGHTMAGENTA_EX}]", "            ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}26{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Youtube Donwloader{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}20{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Editor{Fore.LIGHTMAGENTA_EX}]",  "           ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}27{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}First Page{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}21{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Nitro Gift Checker{Fore.LIGHTMAGENTA_EX}]", "     ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}28{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Next Page{Fore.LIGHTMAGENTA_EX}]")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    if choice == "15":
        TokenMailverifier()
    elif choice == "16":
        clear()
        print(banner)
        pass_changer()
    elif choice == "17":
        online_tokens()
    elif choice == "18":
        clear()
        print(banner)
        status_changer()
    elif choice == "19":
        Token_nuker()
    elif choice == "20":
        token_editor()
    elif choice == "21":
        check_codes()
    elif choice == "22":
        Discord_nuker()
    elif choice == "23":
        get_own_token()
    elif choice == "24":
        token_login()
    elif choice == "25":
        Cleaner()
    elif choice == "26":
        youtube_converter()
    elif choice == "27":
        main()
    elif choice == "28":
        main3()
    main2()

def main3():
    new_title("Nexus MultiTool │ Page 3")
    clear()
    print(banner)
    print("                               ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}29{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Remove Discord Injection{Fore.LIGHTMAGENTA_EX}]", "  ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}36{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Avatar Scraper{Fore.LIGHTMAGENTA_EX}]" )
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}30{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Wartermarker{Fore.LIGHTMAGENTA_EX}]", "        ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}37{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Gen Test Token{Fore.LIGHTMAGENTA_EX}]" )
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}31{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Huminazor{Fore.LIGHTMAGENTA_EX}]", "           ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}38{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Info{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}32{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Payment Checker{Fore.LIGHTMAGENTA_EX}]", "     ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}39{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Ip lookup{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}33{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Leave Groups{Fore.LIGHTMAGENTA_EX}]", "        ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}40{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Socials{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}34{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Guild Count Checker{Fore.LIGHTMAGENTA_EX}]",  " ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}41{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}First Page{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}35{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Message Everywhere{Fore.LIGHTMAGENTA_EX}]", "  ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}42{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Seconde Page{Fore.LIGHTMAGENTA_EX}]")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    if choice == "29":
        print(f"{Fore.RED} CAN BREAK UR DISCORD!!")
        choice1 = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Do u want to go back? (y/n): ")
        if choice1 == "y":
            pass
        else:
            RemoveInjection()
    elif choice == "30":
        token_wartermarker()
    elif choice == "31":
        procces_hm()
    elif choice == "32":
        check_payments()
    elif choice == "33":
        leave_groups()
    elif choice == "34":
        guild_count()
    elif choice == "35":
        meessage_everywhere_spam()
        input("")
    elif choice == "36":
        scrape_Avatars()
    elif choice == "37":
        print(f"{Fore.RED} ONLY GEN ONE OR IT WILL GET LOCKED!")
        print(f"{Fore.RED} DISCORD CANT BE RUNNING IN BACKROUND CLOSE IT!!")
        close_discord = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Did U close discord? (y/n): ")
        if close_discord == "y":
            gen_token()
        else:
            pass
    elif choice == "38":
        token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
        fetch_user_details(token)
    elif choice == "39":
        ip_lookup()
    elif choice == "40":
        social_menu()
    elif choice == "41":
        main()
    elif choice == "42":
        main2()
    main3()

StartupTool()
main()


from Helper import *
from Helper.Common.utils import *

clear()

color = Fore.LIGHTMAGENTA_EX

def change_theme():
    global color
    clear()
    print_banner(color)
    print(f"""
{color}<<{Fore.RESET}1{color}>>  [{Fore.RESET}Light Magenta (Standart){color}]
{color}<<{Fore.RESET}2{color}>>  [{Fore.RESET}Light Blue{color}]
{color}<<{Fore.RESET}3{color}>>  [{Fore.RESET}Light Red{color}]
{color}<<{Fore.RESET}4{color}>>  [{Fore.RESET}Light Green{color}]
{color}<<{Fore.RESET}5{color}>>  [{Fore.RESET}Light Cyan{color}]
{color}<<{Fore.RESET}6{color}>>  [{Fore.RESET}Light Yellow{color}]
{color}<<{Fore.RESET}7{color}>>  [{Fore.RESET}Magenta{color}]
{color}<<{Fore.RESET}8{color}>>  [{Fore.RESET}Blue{color}] 
{color}<<{Fore.RESET}9{color}>>  [{Fore.RESET}Red{color}]
{color}<<{Fore.RESET}10{color}>> [{Fore.RESET}Green{color}]
{color}<<{Fore.RESET}11{color}>> [{Fore.RESET}Cyan{color}]
{color}<<{Fore.RESET}12{color}>> [{Fore.RESET}Yellow{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice: ")
    colors = {
        "1": Fore.LIGHTMAGENTA_EX,
        "2": Fore.LIGHTBLUE_EX,
        "3": Fore.LIGHTRED_EX,
        "4": Fore.LIGHTGREEN_EX,
        "5": Fore.LIGHTCYAN_EX,
        "6": Fore.LIGHTYELLOW_EX,
        "7": Fore.MAGENTA,
        "8": Fore.BLUE,
        "9": Fore.RED,
        "10": Fore.GREEN,
        "11": Fore.CYAN,
        "12": Fore.YELLOW
    }
    color = colors.get(choice)
    if color:
        color = color
    else:
        print("invalid choice")
        time.sleep(1)

def main():
    new_title("Nexus MultiTool │ Page 1")
    clear()
    print_banner(color)
    print(f"""
                    {color}<<{Fore.RESET}1{color}>> [{Fore.RESET}Token Formater{color}]        {color}<<{Fore.RESET}8{color}>>  [{Fore.RESET}Proxy Scraper{color}]         {color}<<{Fore.RESET}15{color}>>  [{Fore.RESET}Token Mail verifier{color}]
                    {color}<<{Fore.RESET}2{color}>> [{Fore.RESET}Token Checker{color}]         {color}<<{Fore.RESET}9{color}>>  [{Fore.RESET}Proxy Checker{color}]         {color}<<{Fore.RESET}16{color}>>  [{Fore.RESET}Token Pass Changer{color}]
                    {color}<<{Fore.RESET}3{color}>> [{Fore.RESET}Token Sorter{color}]          {color}<<{Fore.RESET}10{color}>> [{Fore.RESET}Webhook Tool{color}]          {color}<<{Fore.RESET}17{color}>>  [{Fore.RESET}Token Onliner{color}]
                    {color}<<{Fore.RESET}4{color}>> [{Fore.RESET}Token spammer{color}]         {color}<<{Fore.RESET}11{color}>> [{Fore.RESET}Faker Tool{color}]            {color}<<{Fore.RESET}18{color}>>  [{Fore.RESET}Token Status Rotator{color}]
                    {color}<<{Fore.RESET}5{color}>> [{Fore.RESET}Token Guild Checker{color}]   {color}<<{Fore.RESET}12{color}>> [{Fore.RESET}obfusicator{color}]           {color}<<{Fore.RESET}19{color}>>  [{Fore.RESET}Token Nuker{color}]
                    {color}<<{Fore.RESET}6{color}>> [{Fore.RESET}Token Guild Leaver{color}]    {color}<<{Fore.RESET}13{color}>> [{Fore.RESET}Clear Output Folder{color}]   {color}<<{Fore.RESET}20{color}>>  [{Fore.RESET}Token Editor{color}]
                    {color}<<{Fore.RESET}7{color}>> [{Fore.RESET}Remove Doubles{color}]        {color}<<{Fore.RESET}14{color}>> [{Fore.RESET}Clear Input Folder{color}]    {color}<<{Fore.RESET}21{color}>>  [{Fore.RESET}Nitro Gift Checker{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice: ")
    functions = {
        "1": formater,
        "2": Token_checker,
        "3": sort_tokens,
        "4": token_spammer,
        "5": check_tokens_guild,
        "6": token_leave_server,
        "7": remove_duplicates,
        "8": Proxy_scraper,
        "9": check_proxys,
        "10": Webhook_tool,
        "11": main_faker,
        "12": obfuscate,
        "13": clear_output,
        "14": clear_input,
        "15": TokenMailverifier,
        "16": pass_changer,
        "17": online_tokens,
        "18": status_changer,
        "19": Token_nuker,
        "20": token_editor,
        "21": check_codes,
        "x2": main2,
        "x3": social_menu
    }
    function = functions.get(choice)
    if function:
        function()
    else:
        print("invalid choice")
        time.sleep(1)
    main()

def main2():
    new_title("Nexus MultiTool │ Page 2")
    clear()
    print_banner(color)
    print(f"""
                    {color}<<{Fore.RESET}22{color}>> [{Fore.RESET}Discord Nuker{color}]         {color}<<{Fore.RESET}29{color}>> [{Fore.RESET}Gen Test Token{color}]       {color}<<{Fore.RESET}36{color}>>  [{Fore.RESET}Token WarterMarker{color}]
                    {color}<<{Fore.RESET}23{color}>> [{Fore.RESET}Get Own Token{color}]         {color}<<{Fore.RESET}30{color}>> [{Fore.RESET}Get Token Info{color}]       {color}<<{Fore.RESET}37{color}>>  [{Fore.RESET}Token Huminazor{color}]
                    {color}<<{Fore.RESET}24{color}>> [{Fore.RESET}Token Login{color}]           {color}<<{Fore.RESET}31{color}>> [{Fore.RESET}Simple Ip Lookup{color}]     {color}<<{Fore.RESET}38{color}>>  [{Fore.RESET}Token Payment Checker{color}]
                    {color}<<{Fore.RESET}25{color}>> [{Fore.RESET}Pc Cleaner{color}]            {color}<<{Fore.RESET}32{color}>> [{Fore.RESET}Simple Ip grabber{color}]    {color}<<{Fore.RESET}39{color}>>  [{Fore.RESET}Token Leave Groups{color}]
                    {color}<<{Fore.RESET}26{color}>> [{Fore.RESET}Youtube Donwloader{color}]    {color}<<{Fore.RESET}33{color}>> [{Fore.RESET}Serial Changer{color}]       {color}<<{Fore.RESET}40{color}>>  [{Fore.RESET}Token Guild Count Checker{color}]
                    {color}<<{Fore.RESET}27{color}>> [{Fore.RESET}Id To Token{color}]           {color}<<{Fore.RESET}34{color}>> [{Fore.RESET}Serial Checker{color}]       {color}<<{Fore.RESET}41{color}>>  [{Fore.RESET}Token message everywhere{color}]
                    {color}<<{Fore.RESET}28{color}>> [{Fore.RESET}Avatar Scraper{color}]        {color}<<{Fore.RESET}35{color}>> [{Fore.RESET}Change Theme{color}]         {color}<<{Fore.RESET}42{color}>>  [{Fore.RESET}Discord Message Logger{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice: ")
    functions = {
        "22": Discord_nuker,
        "23": get_own_token,
        "24": token_login,
        "25": Cleaner,
        "26": youtube_converter,
        "27": id__token,
        "28": scrape_Avatars,
        "29": gen_token,
        "30": fetch_user_details,
        "31": ip_lookup,
        "32": make_ip_grabber,
        "33": serial_changer,
        "34": check_serials,
        "35": change_theme,
        "36": token_wartermarker,
        "37": procces_hm,
        "38": check_payments,
        "39": token_leave_server,
        "40": check_tokens_guild,
        "41": meessage_everywhere_spam,
        "42": message_logger,
        "x1": main,
        "x3": social_menu
    }
    function = functions.get(choice)
    if function:
        function()
    else:
        print("invalid choice")
        time.sleep(1)
    main2()

StartupTool()
os.system("mode con cols=135 lines=24")
main()

from Helper import *
from Helper.Common.utils import *

socket.setdefaulttimeout(180)



working = 0
bad = 0


def is_bad_proxy(pip):
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        sock = urllib.request.urlopen('http://google.com')
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as detail:
        return 1
    return 0

def check_proxy(proxy):
    global bad, working
    if is_bad_proxy(proxy):
        print(f"{lc} {Fore.BLUE}Proxy={Fore.WHITE}{proxy}{Fore.RESET} Flags: {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}BAD{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        bad += 1
    else:
        print(f"{lc} {Fore.BLUE}Proxy={Fore.WHITE}{proxy}{Fore.RESET} Flags: {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}WORKING{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        working += 1
        with open("Output/Proxys/working_proxies.txt", 'a', encoding="utf-8") as file:
            file.write(f"{proxy} \n")

def check_proxies_from_file():
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Use Input/proxies.txt?: (y/n) ")
    if choice == "y":
        file_to_check = "Input/proxies.txt"
    else:
        file_to_check = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Drag and drop proxie file to check: ")
    with open(file_to_check, 'r') as file:
        proxyList = file.read().splitlines()
    
    with ThreadPoolExecutor(max_workers=10) as executor:  
        executor.map(check_proxy, proxyList)

def check_proxys():
    new_title("Proxy Checker discord.gg/nexustools")
    with open("Output/Proxys/working_proxies.txt", 'w', encoding="utf-8") as file:
        file.close()
    check_proxies_from_file()
    print(f"{ld} Results: Working Proxies: {Fore.GREEN}{working}{Fore.RESET} Bad Proxies: {Fore.RED}{bad}{Fore.RESET} {Fore.GREEN}Total: {bad + working}{Fore.RESET}")
    input("Press Enter To continue...")

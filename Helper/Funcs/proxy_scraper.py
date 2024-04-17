from Helper import *
from Helper.Common.utils import *



count = 0
idx = 0
def Animation():
    global idx
    animation = "|/-\\"
    print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Loading", animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)

def get_proxys(typ, timeout):
    global count
    for _ in range(25):
        Animation()
    answer = requests.get(f'https://api.proxyscrape.com/v2/?request=displayproxies&protocol={typ}&timeout={timeout}&country=all&ssl=all&anonymity=all')
    if answer.status_code == 200:
        time.sleep(0.5)
    lines = [line.strip() for line in answer.text.splitlines() if line.strip()]
    for line in lines:
        count += 1
        print(f"{lc} {Fore.BLUE}Proxy={Fore.WHITE}{line}{Fore.RESET}")
    filtered_text = '\n'.join(lines)
    with open(f"Output/Proxys/Scraped/{typ}_proxies.txt", 'w', encoding="utf-8") as file:
        file.write(filtered_text)
    print(f"{ld} Proxys Scraped: {Fore.GREEN}{count}{Fore.RESET}")
    input("Press Enter To continue...")

def Proxy_scraper():
    new_title("Proxy Scraper discord.gg/nexustools")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter Type: (http / socks4 / socks5): ")
    if choice == 'http':
        typ = choice
        timeout = '500'
    elif choice == 'socks4':
        typ = choice
        timeout = '1000'
    elif choice == 'socks5':
        typ = choice
        timeout = '1000'
    else:
        print("invalid")
        time.sleep(1)
        Proxy_scraper()
    get_proxys(typ, timeout)



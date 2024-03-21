from Helper import *
from Helper.Common.utils import *

headers = {
    'Content-Type': 'application/json'
}

class ngen:
    def generate_nitro_gifts(webhook_url):
        
        while True:
            valid_gift = random.randint(1, 250)
            for i in range(1, 501):
                code = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(16))
                if i == valid_gift:
                    print(f"{lc} {Fore.BLUE}code={Fore.WHITE}https://discord.gift/{code}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}VALID{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
                    time.sleep(1)
                    payload = {
                    'content': f"https://discord.gift/{code}"
                    }
                    json_payload = json.dumps(payload)
                    try:
                        response = requests.post(webhook_url, data=json_payload, headers=headers)
                        if response.status_code == 200:
                            print(f"{lc} {Fore.BLUE}code={Fore.WHITE}https://discord.gift/{code}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}SEND WITH WEBHOOK{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
                        else:
                            print(f"{lc} {Fore.BLUE}code={Fore.WHITE}https://discord.gift/{code}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}INVALID WEBHOOK{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
                    except:
                        print(f"{lc} {Fore.BLUE}code={Fore.WHITE}https://discord.gift/{code}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}INVALID WEBHOOK{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
                else:
                    print(f"{lc} {Fore.BLUE}code={Fore.WHITE}https://discord.gift/{code}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}INVALID{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
                    time.sleep(0.2)


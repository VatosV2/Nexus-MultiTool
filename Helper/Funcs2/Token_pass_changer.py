from Helper import *
from Helper.Common.utils import *

use_proxies = False
Proxie_file = ""

def check_status(status_code: int):
    status_messages = {
        200: "Success",
        201: "Success",
        204: "Success",
        400: "Detected Captcha",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        405: "Method not allowed",
        429: "Too many Requests"
    }
    return status_messages.get(status_code, "Unknown Status")

def change_pass():

    random_pass = input(f'{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Use Random Password? (y/n): ')
    if random_pass == "y":
        new_pass = generate_password()
    else:
        new_pass = input(f'{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] New Password: ')

    def pwchanger(token, password, email, new_pass):
        url = 'https://discord.com/api/v9/users/@me'
        payload = {'password': password, 'new_password': new_pass}
        headerz = get_headers(token)
        session = tls_client.Session(client_identifier = "chrome_122", random_tls_extension_order=True)
        if use_proxies == True:
            session.proxies = "http://" + GetFormattedProxy(Proxie_file)

        r = session.patch(url, json=payload, headers=headerz)
        if r.status_code == 200:
            new_token = r.json()['token']
            print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}PASSWORD CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
            open("Output/Token_pass_changer/new_tokens.txt", "a").write(f"{email}:{new_pass}:{new_token}\n")
        else:
            print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.RED}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}')

    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]

    with ThreadPoolExecutor(max_workers=10) as executor:
        for account in tokens:
            email, password, token = account.split(':')[:3]
            executor.submit(pwchanger, token, password, email, new_pass)
    input("Press Enter To continue...")


def pass_changer():
    new_title("Token Pass Changer discord.gg/nexustools")
    proxies = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Use Proxies? (y/n): ")
    if proxies == "y":
        print(f"{lc} {Fore.GREEN}Using Proxies!{Fore.RESET}")
        use_proxies = True
        proxie_file_ask = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Use Input/proxies.txt? (y/n): ")
        if proxie_file_ask == "y":
            Proxie_file = "Input/proxies.txt"
        else:
            proxie_file_path = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Drag and Drop Proxie File: ")
            Proxie_file = proxie_file_path
    else:
        print(f"{lc} {Fore.RED}Not Using Proxies{Fore.RESET}")
        use_proxies = False



    change_pass()
    input("Press Enter To continue...")

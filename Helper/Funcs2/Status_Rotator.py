from Helper import *
from Helper.Common.utils import *


status_file = ""

def read_status_texts(filename):
    with open(filename, 'r') as file:
        status_texts = [line.strip() for line in file.readlines()]
    return status_texts

def change_status(token, text):
    headers = get_headers(token)
    setting = {
        'custom_status': {
            'text': text,
        },
    }
    r = requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}SUCCSES{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def status_changer():
    new_title("Token Status Rotator discord.gg/nexustools")
    staus_file_ask = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Status File(Drag & Drop) (H for help): ")
    if staus_file_ask == "H":
        print(f"{lc} Create a Txt file with a name.")
        print(f"{lc} Every Line Is a new status")
        print(f"{lc} Save it. Then Drag and drop it and pres enter.")
        input("Press Enter To continue...")
        clear()
        print(banner)
        status_changer()
    status_file = staus_file_ask
    tokens_ask = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Use Input/tokens.txt(1) File or singel token(2)? (1/2): ")
    if tokens_ask == "1":
        tokens = get_tokens()
        tokens = [token.strip() for token in tokens]
    else:
        tokens = [input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Input token: ")]
    status_texts = read_status_texts(status_file) 
    timefrequency = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Time: ")
    while True:
        for text in status_texts:
            threads = []
            for token in tokens:
                thread = threading.Thread(target=change_status, args=(token, text))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()
            time.sleep(int(timefrequency))  
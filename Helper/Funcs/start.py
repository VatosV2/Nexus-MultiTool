from Helper import *
from Helper.Common.utils import *

Files = [
    'removed_doubles.txt',
    'Valid_Tokens.txt',
    'TokenSorter/email_verified_tokens.txt',
    'TokenSorter/unclaimed_tokens.txt',
    'TokenSorter/fully_verified_tokens.txt',
    'TokenSorter/phone_verified_tokens.txt'
]

dirs = [
    'Proxys',
    'Proxys/Scraped',
    'Obf',
    'Faker',
    'TokenSorter',
    'EmailVerifier',
    'Token_pass_changer',
    'Nuker',
    'gift_codes',
    'Danger',
    'Payment_tokens',
    'Avatars',
    'Token_gen',
    'Youtube',
    'ServerIdChecker'
]


def StartupTool():
    new_title("Nexus Startup discord.gg/nexustools")
    if os.path.exists(f"Output"):
        pass
    else:
        os.makedirs(f"Output")
        print(f"{lc} {Fore.BLUE}Folder={Fore.WHITE}Output{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        time.sleep(0.3)
    for dir in dirs:
        if os.path.exists(f"Output/{dir}"):
            print(f"{lc} {Fore.BLUE}Folder={Fore.WHITE}{dir}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}EXISTS ALREADY{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            time.sleep(0.1)
        else:
            os.makedirs(f"Output/{dir}")
            print(f"{lc} {Fore.BLUE}Folder={Fore.WHITE}{dir}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            time.sleep(0.3)
    for file in Files:
        if os.path.exists(f"Output/{file}"):
            print(f"{lc} {Fore.BLUE}File={Fore.WHITE}{file}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}EXISTS ALREADY{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            time.sleep(0.1)
        else:
            with open(f"Output/{file}", 'w', encoding="utf-8") as f:
                pass
            print(f"{lc} {Fore.BLUE}File={Fore.WHITE}{file}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            time.sleep(0.3)

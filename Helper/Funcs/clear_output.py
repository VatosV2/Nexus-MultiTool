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
    'Youtube'
]

print(banner)

def clear_output():
    new_title("Nexus Clearing Output Folder...")
    for dir in dirs:
        try:
            os.makedirs(f"Output/{dir}")  
        except FileExistsError:
            pass
        for filename in os.listdir(f"Output/{dir}"):
            file_path = os.path.join(f"Output/{dir}", filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)  
                elif os.path.isdir(file_path):
                    os.rmdir(file_path) 
            except Exception as e:
                print(f"{lc} {Fore.BLUE}Folder={Fore.WHITE}{dir}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR WHILE DELETING{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {e}")
                time.sleep(0.3)
        print(f"{lc} {Fore.BLUE}Folder={Fore.WHITE}{dir}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CLEARED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        time.sleep(0.3)
    for file in Files:
        with open(f"Output/{file}", 'w', encoding="utf-8") as f:
            pass
        print(f"{lc} {Fore.BLUE}File={Fore.WHITE}{file}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        time.sleep(0.3)



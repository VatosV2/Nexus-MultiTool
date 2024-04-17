from Helper import *
from Helper.Common.utils import *

mail = 0
phone = 0
unclaimed = 0
full = 0
inv = 0
email_verified_tokens = []
fully_verified_tokens = []
not_verified_tokens = []
phone_verified_tokens = []


def check_token_verification(token):
    global mail, phone, unclaimed, full, inv
    global email_verified_tokens, fully_verified_tokens, not_verified_tokens
    headers = {
        'Authorization': token
    }

    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)

    if response.status_code == 200:
        data = response.json()
        email_verification = data.get('verified', False)
        phone_verification = bool(data.get('phone'))

        if email_verification and phone_verification:
            full += 1
            fully_verified_tokens.append(token)
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLUE_EX}[{Fore.GREEN}Full Verified{Fore.LIGHTBLUE_EX}]{Fore.RESET}")
        elif email_verification:
            mail += 1
            email_verified_tokens.append(token)
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLUE_EX}[{Fore.GREEN}Mail Verified{Fore.LIGHTBLUE_EX}]{Fore.RESET}")
        elif phone_verification:
            phone += 1
            phone_verified_tokens.append(token)
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLUE_EX}[{Fore.GREEN}Phone Verified{Fore.LIGHTBLUE_EX}]{Fore.RESET}")
        else:
            unclaimed += 1
            not_verified_tokens.append(token)
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLUE_EX}[{Fore.GREEN}Unclaimed{Fore.LIGHTBLUE_EX}]{Fore.RESET}")
    elif response.status_code == 401:
        inv += 1
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLUE_EX}[{Fore.RED}INVALID{Fore.LIGHTBLUE_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLUE_EX}[{Fore.RED}ERROR{Fore.LIGHTBLUE_EX}]{Fore.RESET}")
    

def save_tokens_to_file(file_path, tokens):
    with open(file_path, 'w') as file:
        for full_token in tokens:
            file.write(f"{full_token}\n")

def process_tokens(tokens):
    global email_verified_tokens, fully_verified_tokens, not_verified_tokens, phone_verified_tokens

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for token in tokens:
            [executor.submit(check_token_verification, token)]

    save_tokens_to_file("output/TokenSorter/email_verified_tokens.txt", email_verified_tokens)
    save_tokens_to_file("output/TokenSorter/fully_verified_tokens.txt", fully_verified_tokens)
    save_tokens_to_file("output/TokenSorter/phone_verified_tokens.txt", fully_verified_tokens)
    save_tokens_to_file("output/TokenSorter/unclaimed_tokens.txt", not_verified_tokens)

def results():
    print(f"{ld} mail verified tokens: {Fore.GREEN}{mail}{Fore.RESET}")
    print(f"{ld} phone verified tokens: {Fore.GREEN}{phone}{Fore.RESET}")
    print(f"{ld} full verified tokens: {Fore.GREEN}{full}{Fore.RESET}")
    print(f"{ld} unclaimed tokens: {Fore.GREEN}{unclaimed}{Fore.RESET}")
    print(f"{ld} Invalid tokens: {Fore.GREEN}{inv}{Fore.RESET}")
    print(f"{ld} Total Tokens Checked: {Fore.GREEN}{mail + phone + full + unclaimed + inv}{Fore.RESET}")
    input("Press Enter To continue...")

def sort_tokens():
    new_title("Token Sorter discord.gg/nexustools")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Use Token or Valid Token file? (V/T) ")
    if choice == "T":
        tokens = get_tokens()
        tokens = [token.strip() for token in tokens]
    elif choice == "V":
        tokens = get_valid_tokens()
        tokens = [token.strip() for token in tokens]
    else:
        print("invalid choice")
        time.sleep(0.5)
        sort_tokens()

    if tokens:
        process_tokens(tokens)
    else:
        print("No Discord tokens found in the file.")
    results()


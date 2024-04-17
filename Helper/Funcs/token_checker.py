from Helper import *
from Helper.Common.utils import *


os.system("cls")
tokens911 = []
valid_tokens_count = 0
invalid_tokens_count = 0
nitro_count = 0
unclaimed_count = 0
mail_verified_count = 0
phone_verified_count = 0
full_verified_count = 0
locked_count = 0 
total_checks = 0

def check_token_verification(token):
    global tokens, valid_tokens_count, invalid_tokens_count, nitro_count, mail_verified_count, unclaimed_count, full_verified_count
    headers = {
        'Authorization': token
    }

    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)

    if response.status_code == 200:
        data = response.json()
        email_verification = data.get('verified', False)
        phone_verification = bool(data.get('phone'))

        if email_verification and phone_verification:
            full_verified_count += 1
            return f"Full Verified"
        elif email_verification:
            mail_verified_count += 1
            return f"Mail Verified"
        elif phone_verification:
            phone_verified_count += 1
            return f"Phone Verified"
        else:
            unclaimed_count += 1
            return f"Unclaimed"
    elif response.status_code == 401:
        return f"invalid"
    else:
        return f"error"
    
def check_boosts(token):
    headers = {
        'Authorization': f'{token}'
    }

    response = requests.get('https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots', headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:  
            cooldown_count = sum(1 for entry in data if entry.get('cooldown_ends_at') is not None)
            boosts = 2 - int(cooldown_count)
            return boosts
        else:
            return 0
    else:
        return 0


    
def check_token(token):
    global tokens, valid_tokens_count, invalid_tokens_count, nitro_count, mail_verified_count, unclaimed_count, full_verified_count, locked_count, total_checks
    total_checks += 1
    headers = {
        'Authorization': token
    }

    response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if response.status_code == 200:
        
        try:
            r = requests.get("https://discordapp.com/api/v6/users/@me/settings", headers=headers)
            if r.status_code == 200:
                valid_tokens_count += 1
                user_data = response.json()
                premium_type = user_data.get('premium_type', 0)  
                verification = check_token_verification(token)
                boosts = check_boosts(token)
                nitro = f"{Style.BRIGHT}{Fore.RED}NO_NITRO" if premium_type == 0 else f"{Style.BRIGHT}{Fore.GREEN}NITRO"
                if premium_type != 0:
                    nitro_count += 1

                print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Flags: {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}VALID{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.BLUE}{boosts}_BOOSTS{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}, {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.BLUE}{nitro}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}, {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.BLUE}{verification}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}{Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}UNLOCKED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
                tokens911.append(token)
                return True
        except Exception as e:
            print(f"Error processing JSON: {e}")
            return False
        else:
            locked_count += 1
            print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Flags: {Fore.RESET}{Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.YELLOW}LOCKED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')

    else:
        invalid_tokens_count += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Flags: {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}INVALID{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')

    

def Token_checker():
    new_title("Token Checker discord.gg/nexustools")
    tokens = get_tokens()

    tokens = [token.strip() for token in tokens]
    num_threads = 8
    total_tokens = len(tokens)
    tokens_per_thread = total_tokens // num_threads

    def check_tokens_worker(start, end):

        for i in range(start, end):
            token = tokens[i]
            check_token(token)
    threads = []
    for i in range(num_threads):
        start = i * tokens_per_thread
        end = (i + 1) * tokens_per_thread if i < num_threads - 1 else total_tokens
        thread = threading.Thread(target=check_tokens_worker, args=(start, end))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    with open("Output/Valid_Tokens.txt", "w", encoding="utf-8") as file:
        for token in tokens911:
            file.write(f"{token}\n")
    print(f"{ld}Valid Tokens: {Fore.GREEN}{valid_tokens_count}{Fore.RESET}")
    print(f"{ld}Invalid Tokens: {Fore.GREEN}{invalid_tokens_count}{Fore.RESET}")
    print(f"{ld}Locked: {Fore.GREEN}{locked_count}{Fore.RESET}")
    print(f"{ld}Nitro: {Fore.GREEN}{nitro_count}{Fore.RESET}")
    print(f"{ld}Uncalimed: {Fore.GREEN}{unclaimed_count}{Fore.RESET}")
    print(f"{ld}Mail Verified: {Fore.GREEN}{mail_verified_count}{Fore.RESET}")
    print(f"{ld}Phone Verified: {Fore.GREEN}{phone_verified_count}{Fore.RESET}")
    print(f"{ld}Full Verified: {Fore.GREEN}{full_verified_count}{Fore.RESET}")
    print(f"{ld}Total: {Fore.GREEN}{total_checks}{Fore.RESET}")
    input("Press Enter To continue...")



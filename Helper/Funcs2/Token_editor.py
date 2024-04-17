from Helper import *
from Helper.Common.utils import *

avatar_path = ""

def update_bio(discord_token, new_bio,):
    headers = get_headers(discord_token)
    payload = {"bio": f"{new_bio}"}
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)

    r = session.patch("https://discord.com/api/v9/users/@me", json=payload, headers=headers)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}BIO CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")


def Change_lang(discord_token, lang):
    payload = {"locale": lang}
    headers = get_headers(discord_token)
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    r = session.patch("https://discord.com/api/v9/users/@me/settings", json=payload, headers=headers)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}LANGUAGE CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")



def Change_name(discord_token, new_nickname):
    payload = {'global_name': new_nickname}
    headers = get_headers(discord_token)
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    r = session.patch("https://discord.com/api/v9/users/@me", json=payload, headers=headers)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}NAME CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")


def pronoun_changer(token, nouns):
    headerz = get_headers(token)
    payload = {"pronouns":  nouns}
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    r = session.patch("https://discord.com/api/v9/users/@me/profile", json=payload, headers=headerz)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}PRONOUN CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def get_avatar(path):
    path2 = os.getcwd()
    picture = [f for f in os.listdir(path2 + f"\{path}") if isfile(join(path2 + f"\{path}", f))]
    random_picture = random.choice(picture)
    with open(f"{path}\\{random_picture}", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode('utf-8')

def change_avatar(token, path):
    avatar_data = get_avatar(path)
    session = Session(client_identifier="chrome_122", random_tls_extension_order=True)

    headers = get_headers(token)

    data = {
        "avatar": f"data:image/jpeg;base64,{avatar_data}"
    }

    response = session.patch("https://discord.com/api/v9/users/@me", json=data, headers=headers)

    if response.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}PFP CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{response.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def process_tokens(target, arg1):
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    threads = []
    for token in tokens:
        token = token.strip()
        thread = threading.Thread(target=target, args=(token, arg1))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    input("Press Enter To continue...")
    token_editor()

def token_editor():
    new_title("Token Editor discord.gg/nexustools")
    
    clear()
    print(banner)
    print(f"{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}] Change Bio")
    print(f"[{Fore.MAGENTA}2{Fore.RESET}] Change Name")
    print(f"[{Fore.MAGENTA}3{Fore.RESET}] Change Pronouns")
    print(f"[{Fore.MAGENTA}4{Fore.RESET}] Change PFP")
    print(f"[{Fore.MAGENTA}5{Fore.RESET}] Change language")
    print(f"[{Fore.MAGENTA}0{Fore.RESET}] Leave")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    if choice == "1":
        print(banner)
        clear()
        bio = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] New Bio: ")
        process_tokens(update_bio, bio)
    elif choice == "2":
        print(banner)
        clear()
        Name = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] New Name: ")
        process_tokens(Change_name, Name)
    elif choice == "3":
        print(banner)
        clear()
        pronouns = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] New Pronouns: ")
        process_tokens(pronoun_changer, pronouns)
    elif choice == "4":
        print(banner)
        clear()
        avatar_path_ask = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Use Own Pictures?(y/n): ")
        if avatar_path_ask == "n":
            avatar_path = os.path.join('Data', "Avatars", "Preset")
        else:
            avatar_path = os.path.join('Data', "Avatars")
        process_tokens(change_avatar, avatar_path)
    elif choice == "5":
        print(banner)
        clear()
        print(f"""
{Fore.BLUE}Language codes:{Fore.RESET}
              
{Fore.CYAN}United Kingdom{Fore.RESET} -> {Fore.GREEN}en-GB{Fore.RESET}
{Fore.CYAN}France{Fore.RESET} -> {Fore.GREEN}fr{Fore.RESET}
{Fore.CYAN}Germany{Fore.RESET} -> {Fore.GREEN}de{Fore.RESET}
{Fore.CYAN}Italy{Fore.RESET} -> {Fore.GREEN}it{Fore.RESET}
{Fore.CYAN}Netherlands{Fore.RESET} -> {Fore.GREEN}nl{Fore.RESET}
{Fore.CYAN}Brazil{Fore.RESET} -> {Fore.GREEN}pt-BR{Fore.RESET}
{Fore.CYAN}Russia{Fore.RESET} -> {Fore.GREEN}ru{Fore.RESET}
{Fore.CYAN}Japan{Fore.RESET} -> {Fore.GREEN}ja{Fore.RESET}
{Fore.CYAN}South Korea{Fore.RESET} -> {Fore.GREEN}ko{Fore.RESET}
{Fore.CYAN}China (Simplified){Fore.RESET} -> {Fore.GREEN}zh-CN{Fore.RESET}
{Fore.CYAN}China (Traditional){Fore.RESET} -> {Fore.GREEN}zh-TW{Fore.RESET}
{Fore.CYAN}Turkey{Fore.RESET} -> {Fore.GREEN}tr{Fore.RESET}
{Fore.CYAN}Denmark{Fore.RESET} -> {Fore.GREEN}da{Fore.RESET}
{Fore.CYAN}Finland{Fore.RESET} -> {Fore.GREEN}fi{Fore.RESET}
        """)    
        lang = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Language code:")
        process_tokens(Change_lang, lang)
        
    elif choice == "0":
        quit1()
    else:
        print("Invalid")
        time.sleep(1)
        token_editor()
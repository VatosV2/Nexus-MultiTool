from Helper import *
from Helper.Common.utils import *

avatar_path = ""

def update_bio(discord_token, new_bio,):
    session = requests.Session()
    headerz = get_headers(discord_token)
    payload = {"bio": f"{new_bio}"}
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)

    r = session.patch("https://discord.com/api/v9/users/@me", json=payload, headers=headerz)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}BIO CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
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
    response = session.patch("https://discord.com/api/v9/users/@me/profile", json=payload, headers=headerz)
    if response.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}PRONOUN CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{response.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

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

def token_wartermarker():
    new_title("Token Wartermarker discord.gg/nexustools")
    Wartermark = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Invite Code: ")
    if ".gg/" in Wartermark:
        Wartermark = str(Wartermark).split(".gg/")[1]
    elif "invite/" in Wartermark:
        Wartermark = str(Wartermark).split("invite/")[1]
    pic = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Is ur Picture in Data/Avatars? (y/n): ")
    process_tokens(Change_name, f".gg/{Wartermark}")
    process_tokens(update_bio, f"discord.gg/{Wartermark}")
    process_tokens(pronoun_changer, f"discord.gg/{Wartermark}")
    if pic == "y":
        avatar_path = os.path.join('Data', "Avatars")
        process_tokens(change_avatar, avatar_path)
    else:
        pass
    input("Press Enter To continue...")


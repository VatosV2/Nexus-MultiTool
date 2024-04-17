from Helper import *
from Helper.Common.utils import *


used_usernames = []
total_usernames = len(open('data/usernames.txt', encoding='utf-8').read().splitlines())

def generate_username():
    with open('data/usernames.txt', encoding='utf-8') as file:
        usernames = file.read().splitlines()
    available_usernames = [username for username in usernames if username not in used_usernames]
    if len(used_usernames) == total_usernames:
            used_usernames.clear()
    if not available_usernames:
        used_usernames.clear()
        available_usernames = usernames
    username = random.choice(available_usernames)
    used_usernames.append(username)
    return username

def update_bio(discord_token):
    new_bio = random.choice(open('data/bios.txt', encoding="utf-8").readlines()).strip()
    session = requests.Session()
    headerz = get_headers(discord_token)
    payload = {"bio": f"{new_bio}"}
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)

    r = session.patch("https://discord.com/api/v9/users/@me", json=payload, headers=headerz)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}BIO CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def pronoun_changer(token):
    nouns = random.choice(["he/him", "she/her","they/them","Switched/On" , "Ask me","it/its","Cool/Hot"])
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
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)

    headers = get_headers(token)

    data = {
        "avatar": f"data:image/jpeg;base64,{avatar_data}"
    }

    response = session.patch("https://discord.com/api/v9/users/@me", json=data, headers=headers)

    if response.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}PFP CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{response.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def Change_name(discord_token):
    new_nickname = generate_username()
    payload = {'global_name': new_nickname}
    headers = get_headers(discord_token)
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    r = session.patch("https://discord.com/api/v9/users/@me", json=payload, headers=headers)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}NAME CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def hm(token):
    path = os.path.join("data", 'Avatars', "preset")
    change_avatar(token, path)
    pronoun_changer(token)
    update_bio(token)
    Change_name(token)
          
def procces_hm():
    new_title("Token Huminazor discord.gg/nexustools")
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    for token in tokens:
        hm(token)
    input("Press Enter To continue...")
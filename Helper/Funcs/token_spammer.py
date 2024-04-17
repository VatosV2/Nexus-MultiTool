from Helper import *
from Helper.Common.utils import *

lc = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.LIGHTMAGENTA_EX}N{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}"

session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
session.keep_alive = True

def send_message(token, channel_id, payload):
    global session
    header = {
        'authorization': token
    }
    try:
        r = session.post(f"https://discord.com/api/v8/channels/{channel_id}/messages", json=payload, headers=header)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred with token: {token}\n{e}")
        return

    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}[{Fore.GREEN}Message sent{Fore.LIGHTBLACK_EX}]")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Failed to send message. -> {Fore.LIGHTBLACK_EX}({r.status_code})")


def token_spammer():
    new_title("Token Spammer discord.gg/nexustools")
    channel_id = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Input channel ID (Token must be in server): ")
    content = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}]Input message to send: ")
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    payload = {
        'content': content
    }

    while True:
        with ThreadPoolExecutor() as executor:
            for token in tokens:
                executor.submit(send_message, token, channel_id, payload)


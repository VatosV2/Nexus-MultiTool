
from Helper import *
from Helper.Common.utils import *

lc = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.LIGHTMAGENTA_EX}N{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}"




def send_message(token, channel_id, payload):
    header = {'authorization': token}

    try:
        r = requests.post(f"https://discord.com/api/v8/channels/{channel_id}/messages",
                          data=payload, headers=header)
    except requests.exceptions.RequestException as e:
        print("Error occurred with token: " + token)
        print(e)
        return

    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Message sent successfully with token: " + token)
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Failed to send message. Status code: {r.status_code}")


def token_spammer():
    new_title("Nexus Token Spammer")
    channel_id = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Input channel ID (Token must be in server): ")
    content = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}]Input message to send: ")
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    payload = {
        'content': content
    }
    clear()

    while True:
        with ThreadPoolExecutor() as executor:
            for token in tokens:
                executor.submit(send_message, token, channel_id, payload)
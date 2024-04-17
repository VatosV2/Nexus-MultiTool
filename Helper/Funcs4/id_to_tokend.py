from Helper import *
from Helper.Common.utils import *


def id__token():
    new_title("Id to token discord.gg/nexustools")
    id = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Id: ")
    encoded_bytes = base64.urlsafe_b64encode(id.encode("utf-8"))
    token = encoded_bytes.decode("utf-8").rstrip("=")

    print(f"{lc} {Fore.LIGHTMAGENTA_EX}{id} -> {Fore.LIGHTBLUE_EX}{token}")
    input("Press Enter To continue...")

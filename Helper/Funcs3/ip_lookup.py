from Helper import *
from Helper.Common.utils import *

def ip_lookup():
    new_title("Ip lookup discord.gg/nexustools")
    ip = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] IP Address: ")
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    print(f"{lc} Ip: {ip}")
    print(f"{lc} Country: " + data['country'])
    print(f"{lc} City: " + data['city'])
    print(f"{lc} Region: " + data['regionName'])
    print(f"{lc} ISP: " + data['isp'])
    input("Press Enter To continue...")

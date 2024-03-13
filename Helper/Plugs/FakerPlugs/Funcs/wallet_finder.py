from Helper import *
from Helper.Common.utils import *

def generate_wallet(wallet_type):
    alphabet = string.ascii_letters + string.digits
    if wallet_type == "btc":
        prefix = "bc1"
    elif wallet_type == "ltc":
        prefix = "ltc"
    elif wallet_type == "eth":
        prefix = "0x"
    else:
        raise ValueError("Invalid wallet type. Supported types are 'btc', 'ltc', and 'eth'.")
    wallet = prefix + ''.join(random.choices(alphabet, k=32))
    return wallet

def wallet_finer():
    while True:
        wallet_type = random.choice(["btc", "ltc", "eth"])
        wallet = generate_wallet(wallet_type)
        if random.randint(1, 400) == 1:  
            print(f"{Fore.GREEN}{wallet} {Fore.RED}({random.randint(250, 2000)},00$){Fore.RESET}")
            print(f"{lc} Valid {wallet_type} Wallet found!!")
            choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] do you want to continue? (y/n): ")
            if choice == "n":
                exit()
        else:
            print(f"{wallet}  {Fore.RED}(0,00$){Fore.RESET}")
        time.sleep(0.05)

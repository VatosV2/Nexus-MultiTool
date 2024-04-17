from Helper import *
from Helper.Common.utils import *

hidden_valids = False

def time_difference_in_words(date_string):
    try:
        date = datetime.fromisoformat(date_string)
        now = datetime.now(pytz.utc)

        date = date.replace(tzinfo=pytz.utc)

        time_difference = date - now

        seconds = time_difference.total_seconds()
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds = divmod(remainder, 60)

        if hours > 0:
            return f"{hours} Hours"
        elif minutes > 0:
            return f"{minutes} Minutes"
        elif seconds > 0:
            return f"{seconds} Seconds"
        else:
            return "Now"

    except ValueError:
        return "Idk Bro"
    
def check_discord_gift_code(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        uses = data.get("uses", 0)
        expiration = f'{data["expires_at"]}'
        time_left = time_difference_in_words(expiration)
        plan = data["subscription_plan"]["name"]
        if uses == 0:
            if hidden_valids == True:
               print(f"")
               print((Fore.LIGHTMAGENTA_EX + time.strftime('[%H:%M:%S] ')) + Fore.LIGHTGREEN_EX + f'Valid' + Fore.WHITE + f' | Link:' + Fore.LIGHTCYAN_EX + f'https://discord.gift/hiddenlink' + Fore.WHITE + f' | Expires:' + Fore.LIGHTCYAN_EX + f'{time_left}' + Fore.WHITE + f' | Type:' + Fore.LIGHTCYAN_EX + plan)
            else:
               print((Fore.LIGHTMAGENTA_EX + time.strftime('[%H:%M:%S] ')) + Fore.LIGHTGREEN_EX + f'Valid' + Fore.WHITE + f' | Link:' + Fore.LIGHTCYAN_EX + f'https://discord.gift/{code}' + Fore.WHITE + f' | Expires:' + Fore.LIGHTCYAN_EX + f'{time_left}' + Fore.WHITE +  f' | Type:' + Fore.LIGHTCYAN_EX + plan)
            with open("output/gift_codes/ValidCodes.txt", "a") as valid_file:
                valid_file.write(f"https://discord.gift/{code}\n")
        else:
            print((Fore.LIGHTMAGENTA_EX + time.strftime('[%H:%M:%S] ')) + Fore.YELLOW + f'Claimed' + Fore.WHITE + f' | Link:' + Fore.LIGHTCYAN_EX + f'https://discord.gift/{code}')
            with open("output/gift_codes/UsedGifts.txt", "a") as used_file:
                used_file.write(f"https://discord.gift/{code}\n")
    elif response.status_code == 429:
        print(Fore.CYAN + "Rate Limited | Waiting...")
        time.sleep(3)
        check_discord_gift_code(code)  
    elif response.status_code == 404:
        print((Fore.LIGHTMAGENTA_EX + time.strftime('[%H:%M:%S] ')) +Fore.RED + f'InValid' + Fore.WHITE + f' | Link:' + Fore.LIGHTCYAN_EX + f'https://discord.gift/{code}')
        with open("output/gift_codes/InvalidCodes.txt", "a") as invalid_file:
            invalid_file.write(f"https://discord.gift/{code}\n")
    else:
        print((Fore.LIGHTMAGENTA_EX + time.strftime('[%H:%M:%S] ')) +Fore.RED + f'Unknown' + Fore.WHITE + f' | Link:' + Fore.LIGHTCYAN_EX + f'https://discord.gift/{code}')
        with open("output/gift_codes/UnknownCodes.txt", "a") as unknown_file:
            unknown_file.write(f"https://discord.gift/{code}\n")

def process_gift_codes():
    with open("Input/gift_codes.txt", "r") as file:
        gift_codes = file.readlines()
        gift_codes = [code.strip() for code in gift_codes]
        for code in gift_codes:
            if code.startswith("https://discord.gift/"):
                code = code.replace("https://discord.gift/", "")
                time.sleep(1)
                check_discord_gift_code(code)


def check_codes():
    new_title("Nitro Gift Checker discord.gg/nexustools")
    hidden_valids_ask = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Hide Valids?(y/n): ")
    if hidden_valids_ask == "y":
        hidden_valids == True
    if hidden_valids_ask == "n":
        hidden_valids == False
    process_gift_codes()
    

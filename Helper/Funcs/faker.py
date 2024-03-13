from Helper.Plugs.FakerPlugs import *
from Helper import *
from Helper.Common.utils import *

def generate_token():
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
    secret = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    secret2 = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    return f"MTEx{secret2}.{secret}.{token}"

def gen_token():
    clear()
    with open("Output/Faker/tokens.txt", "a") as tokens_file:
        for _ in range(99999):
            email = gen.generate_email()
            password = gen.generate_password()
            print(f"{lc} Creating Gmail..")
            time.sleep(1.5)
            print(f"{lc} {Fore.BLUE}mail={Fore.WHITE}{email}{Fore.RESET} {Fore.BLUE}password={Fore.WHITE}{password}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED MAIL{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            token = generate_token()
            print(f"{lc} Creating Discord Account..")
            time.sleep(1)
            print(f"{lc} Detected Captcha")
            time.sleep(1)
            print(f"{lc} Solving captcha...")
            time.sleep(1.5)
            account = f"{email}:{password}:{token}"
            print(f"{lc} {Fore.BLUE}Account={Fore.WHITE}{account}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED ACCOUNT{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            tokens_file.write(account + "\n")
            tokens_file.flush() 
            print(f"{ld} Saving token in tokens.txt")
            print(f"{ld} Generating next token...")


def fake_ddos():
    clear()
    target_ip = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter ip to attack: ")
    ddos.fake_ddoser(target_ip)

def fake_nitro_gen():
    webhook_url = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter webhook url: ")
    ngen.generate_nitro_gifts(webhook_url)

def main_faker():
    clear()
    print(banner)
    print()
    print()
    print(Fore.BLUE + "                                                1. Fake Token Gen")
    print(Fore.BLUE + "                                                2. Dake ddos attack")
    print(Fore.BLUE + "                                                3. Fake Nitro gen")
    print(Fore.BLUE + "                                                4. Fake Identity")
    print(Fore.BLUE + "                                                5. Fake Gmail Gen")
    print(Fore.BLUE + "                                                6. Fake CC")
    print(Fore.BLUE + "                                                7. Fake Wallet Finder")
    print(Fore.BLUE + "                                                8. Fake Social Botter")
    print(Fore.BLUE + "                                                0. Exit")
    print() 
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    if choice == '1':
        gen_token()
    if choice == '2':
        fake_ddos()
    if choice == '3':
        fake_nitro_gen()
    if choice == '4':
        person.create_fake_profile()
        main_faker()
    if choice == '5':
        emailgen()
    if choice == "6":
        generate_fake_credit_card_info()
    elif choice == "7":
        wallet_finer()
    elif choice == "8":
        fake_social_bot()
    if choice == "0":
        quit1()
    else:
        print("invalid")
        time.sleep(1)
        main_faker()
    


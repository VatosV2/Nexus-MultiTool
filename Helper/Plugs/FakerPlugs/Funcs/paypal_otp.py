from Helper import *
from Helper.Common.utils import *

def paypal_otp():
    phone_prefix = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Phone prefix: ")
    os.system("cls")
    print(banner)
    email_pass = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Email:pass: ")
    phone_number = ''.join(str(random.randint(0, 9)) for _ in range(10))
    phone_number2 = ''.join(str(random.randint(0, 9)) for _ in range(10))
    print(f"""
{Fore.LIGHTBLUE_EX}- {Fore.GREEN}Making Call... 
{Fore.LIGHTBLUE_EX}- {Fore.CYAN}Number: {phone_prefix} {phone_number}    
{Fore.LIGHTBLUE_EX}- {Fore.CYAN}Calling id: +555 {phone_number2}{Fore.RESET}
""")
    time.sleep(4.5)
    print(f"{Fore.LIGHTBLUE_EX}- {Fore.GREEN}Caller Picked Up..{Fore.RESET}")
    time.sleep(3)
    verification_code = ''.join(str(random.randint(0, 9)) for _ in range(6))
    print(f"{Fore.LIGHTBLUE_EX}- {Fore.CYAN}Verification Code: {Fore.GREEN}{verification_code}")
    input("Press Enter To continue...")

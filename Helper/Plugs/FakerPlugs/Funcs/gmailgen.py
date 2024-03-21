from Helper import *
from Helper.Common.utils import *

def clear():
    os.system("cls" if "nt" else "clear")

class gen:
    def generate_email():
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))
        return f"{email}@gmail.com"
    
    def generate_password():
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=14))
        return password

def emailgen():
    clear()
    with open("Output/Faker/gmail.txt", "a") as tokens_file:
        for _ in range(99999):
            print(f"{lc} Creating Gmail..")
            time.sleep(1)
            email = gen.generate_email()
            password = gen.generate_password()
            account = f"{email}:{password}"
            tokens_file.write(account + "\n")
            tokens_file.flush() 
            print(f"{lc} {Fore.BLUE}mail={Fore.WHITE}{email}{Fore.RESET} {Fore.BLUE}password={Fore.WHITE}{password}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED MAIL{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")

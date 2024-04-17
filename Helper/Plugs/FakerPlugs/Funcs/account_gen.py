from Helper import *
from Helper.Common.utils import *

class gen:
    def generate_email():
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))
        return f"{email}@gmail.com"
    
    def generate_password():
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=14))
        return password

def random_time():
    time = random.uniform(0.7, 1.6)
    return time
def epic_games_gen():
    with open ("Output/Faker/epicgames.txt", "a", encoding="utf-8") as w:
        pass
    while True:
        mail = gen.generate_email()
        password = gen.generate_password()
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.YELLOW}https://www.epicgames.com/id/login")
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.YELLOW}Getting Mail.. ")
        time_wait = random_time()
        time.sleep(time_wait)
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.GREEN}Mail: {Fore.CYAN}{mail}")
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.GREEN}Password: {Fore.CYAN}{password}")
        time_wait = random_time()
        time.sleep(time_wait)
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.YELLOW}Solving Hcaptcha..")
        time_wait = random.uniform(3,7)
        time.sleep(time_wait)
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.GREEN}Captcha Solved {Fore.CYAN}in -> {Fore.LIGHTBLACK_EX}{time_wait}")
        time_wait = random_time()
        time.sleep(time_wait)
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.GREEN}Account generated: {Fore.CYAN}{mail}:{password}")
        with open ("Output/Faker/epicgames.txt", "a", encoding="utf-8") as w:
            w.write(f"{mail}:{password}\n")
    
def fortnite_gen():
    with open ("Output/Faker/fortnite.txt", "a", encoding="utf-8") as w:
        pass
    while True:
        mail = gen.generate_email()
        password = gen.generate_password()
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.YELLOW}https://www.epicgames.com/id/login")
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.YELLOW}Getting Mail.. ")
        time_wait = random_time()
        time.sleep(time_wait)
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.GREEN}Mail: {Fore.CYAN}{mail}")
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.GREEN}Password: {Fore.CYAN}{password}")
        time_wait = random_time()
        time.sleep(time_wait)
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.YELLOW}Solving Hcaptcha..")
        time_wait = random.uniform(3,7)
        time.sleep(time_wait)
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.GREEN}Captcha Solved {Fore.CYAN}in -> {Fore.LIGHTBLACK_EX}{time_wait}")
        time_wait = random_time()
        time.sleep(time_wait)
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.GREEN}Account generated: {Fore.CYAN}{mail}:{password}")
        time_wait = random_time()
        time.sleep(time_wait)
        print(f"{Fore.LIGHTBLUE_EX}- {Fore.YELLOW}Adding Fortnite...")
        time_wait = random_time()
        time.sleep(time_wait)
        print(f"{Fore.LIGHTBLUE_EX}- Fortnite added.")
        with open ("Output/Faker/fortnite.txt", "a", encoding="utf-8") as w:
            w.write(f"{mail}:{password}\n")

def fake_account_gen():
    clear()
    print(f"""
    {Fore.LIGHTBLUE_EX}1. {Fore.RED}Epic games
    {Fore.LIGHTBLUE_EX}2. {Fore.RED}Fortnite
    """)
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    functions = {
        "1": epic_games_gen,
        "2": fortnite_gen,
    }
    function = functions.get(choice)
    if function:
        function()
    else:
        print("invalid choice")
        time.sleep(1)
    fake_account_gen()
from Helper import *
from Helper.Common.utils import *

class DiscordAccountCreator:
    def __init__(self):
        self.option = uc.ChromeOptions()
        self.driver = uc.Chrome(options=self.option)
        self.used_usernames = []
        self.total_usernames = len(open('data/usernames.txt', encoding='utf-8').read().splitlines())

    def generate_password(self, length=8):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_username(self):
            with open('data/usernames.txt', encoding='utf-8') as file:
                usernames = file.read().splitlines()
            available_usernames = [username for username in usernames if username not in self.used_usernames]
            if len(self.used_usernames) == self.total_usernames:
                self.used_usernames.clear()
            if not available_usernames:
                self.used_usernames.clear()
                available_usernames = usernames
            username = random.choice(available_usernames)
            self.used_usernames.append(username)
            return username
    
    def create_account(self):
        try:
            self.driver.get("https://discord.com/invite/DFUAh7qcVZ")
            time.sleep(2)

            username = self.generate_username()
            displayname_field = self.driver.find_element('name', 'global_name')
            print(f"{lc} Inputing username: {username}")
            displayname_field.send_keys(username)

            continue_button = self.driver.find_element('css selector', 'button.button__5573c')

            checkbox = self.driver.find_element('css selector', 'input.input__52838')
            checkbox.click()
            print(f"{lc} Clicked Checkbox")

            time.sleep(1)
            continue_button.click()
            print(f"{lc} Clicked Continue")
            token = None
            print(f"{lc} Waiting for token...")
            while token is None:
                token = self.driver.execute_script("""return (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()""")
                if token is None:
                    pass
                else:
                    print(f'{lc} Token: {token}')
                    with open("Output/Token_gen/tokens.txt", 'a', encoding="utf-8") as File:
                        File.write(token)
                        File.write("\n")
                        File.close()

            time.sleep(5)
            print(f"{Fore.RED} MAKE SURE TO INPUT BIRTDAY IF IT POPS UP!!")
            print("")
            print(f"{Fore.RED} IF IT NEED MAIL VERIFICATION GO ON https://mail.tm/ !")
            input("Press Enter To continue...")
            self.driver.quit()

        except Exception as e:
            print("Error creating account:", e)


def gen_test_token():
        new_title("Gen Test Token discord.gg/nexustools")
        print(f"{Fore.RED} ONLY GEN ONE OR IT WILL GET LOCKED!")
        print(f"{Fore.RED} DISCORD CANT BE RUNNING IN BACKROUND CLOSE IT!!")
        close_discord = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Did U close discord? (y/n): ")
        if close_discord == "y":
            gen_token()
        else:
            pass

def gen_token():
    account_creator = DiscordAccountCreator()
    account_creator.create_account()
    input("faf")

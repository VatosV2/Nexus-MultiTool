from Helper.Plugs.FakerPlugs import *
from Helper import *
from Helper.Common.utils import *

def explanation():
    print(f"""
{Fore.LIGHTBLUE_EX}--------------------------------------------------------------------------------------------------
{Fore.RED}          
What is it?
Nexus Faker Tool, None of the functions in this tool Does work.
Its fake and mostly consits of prints.

{Fore.LIGHTBLUE_EX}--------------------------------------------------------------------------------------------------
{Fore.RED}           
Why did i make it?
So u can flex infront of skids that belive everything or scam and make money with it idc.
          
{Fore.LIGHTBLUE_EX}--------------------------------------------------------------------------------------------------
{Fore.RED} 
Nigga?
yes.

{Fore.LIGHTBLUE_EX}--------------------------------------------------------------------------------------------------
          
""")
    input("")
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
    new_title("Faker Tool discord.gg/nexustools")
    clear()
    print(banner)
    print(f"""{Fore.BLUE}
                                    1. Fake Token Gen        7.  Fake Social Botter
                                    2. Fake ddos attack      8.  Fake Wallet Finder
                                    3. Fake Nitro gen        9.  Fake Paypal Otp
                                    4. Fake Identity         10. Fake Account gen
                                    5. Fake Gmail Gen        11. Fake Fn Checker
                                    6. Fake CC               12. Explanation
                                        
                                                      0. Exit
                                                
""")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    functions = {
        "1": gen_token,
        "2": fake_ddos,
        "3": fake_nitro_gen,
        "4": person.create_fake_profile,
        "5": emailgen,
        "6": generate_fake_credit_card_info,
        "7": fake_social_bot,
        "8": wallet_finer,
        "9": paypal_otp,
        "10": fake_account_gen,
        "11": checker,
        "12": explanation,

    }
    function = functions.get(choice)
    if function:
        function()
        main_faker()
    elif choice == "0":
        quit1()
    else:
        print("invalid choice")
        time.sleep(1)
    

from Helper import *
from Helper.Common.utils import *

def check_webhook():
    clear()
    webhook_url = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter the Discord webhook URL you want to check: ")
    response = requests.get(webhook_url)

    if response.status_code == 200:
        print(f"{lc} {Fore.BLUE}Webhook={Fore.WHITE}{webhook_url[:80]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}VALID{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}Webhook={Fore.WHITE}{webhook_url[:80]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}INVALID{response.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")

    input("Press Enter To continue...")
    Webhook_tool()


def send_discord_message(webhook_url, message):
    payload = {
        "content": message
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print(f"{lc} {Fore.BLUE}Webhook={Fore.WHITE}{webhook_url[:80]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}Message Send{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}Webhook={Fore.WHITE}{webhook_url[:80]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}FAILED: {response.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")

def webhook_spammer():
    clear()
    webhook_url = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter your Discord webhook URL: ")
    message = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter the message you want to send: ")

    frequency_option = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Select the sending frequency option (fast / normal / slow): ")

    if frequency_option == "fast":
        frequency = 0.01  
        clear()
    elif frequency_option == "normal":
        frequency = 1  
        clear()
    elif frequency_option == "slow":
        clear()
        frequency = 5 
        clear()
    else:
        print("Invalid")
        frequency = 0.01

    while True:
        send_discord_message(webhook_url, message)
        time.sleep(frequency)

def delete_webhook():
    clear()
    webhook_url = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter your Discord webhook URL: ")
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print(f"{lc} {Fore.BLUE}Webhook={Fore.WHITE}{webhook_url[:80]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}Webhook Deleted{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        input("Press Enter To continue...")
        Webhook_tool()
    else:
        print("Failed to delete webhook.")
        print(f"{lc} {Fore.BLUE}Webhook={Fore.WHITE}{webhook_url[:80]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}FAILED: {response.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        input("Press Enter To continue...")
        Webhook_tool()
        
def send_message():
    clear()
    webhook_url = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter your Discord webhook URL: ")
    message = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter the message you want to send: ")
    send_discord_message(webhook_url, message)
    input("Press Enter To continue...")
    Webhook_tool()
               
def Webhook_tool():
    new_title("Nexus Webhook Tool")
    clear()
    print(banner)
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}1{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Spammer{Fore.LIGHTMAGENTA_EX}]")
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}2{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Deleter{Fore.LIGHTMAGENTA_EX}]")
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}3{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Send Message{Fore.LIGHTMAGENTA_EX}]")
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}4{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Check Webhook{Fore.LIGHTMAGENTA_EX}]")
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}5{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Exit{Fore.LIGHTMAGENTA_EX}]")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    if choice == "1":
        webhook_spammer()
    if choice == "2":
        delete_webhook()
    if choice == "3":
        send_message()
    if choice == "4":
        check_webhook()
    if choice == "5":
        quit1()
    else:
        print("Invalid")
        time.sleep(1)
        Webhook_tool()



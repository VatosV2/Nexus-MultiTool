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


def send_discord_message(webhook_url, message, frequency=0.1):
    payload = {
        "content": message
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print(f"{lc} {Fore.BLUE}Webhook={Fore.WHITE}{webhook_url[:80]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}Message Send{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}Webhook={Fore.WHITE}{webhook_url[:80]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}FAILED: {response.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    time.sleep(frequency)

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
        send_discord_message(webhook_url, message, frequency)

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

def webhook_spammer_multiple():
    print("Choose Webhook file in window.")
    webhook_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    print(f"Webhook file: {webhook_file}")
    message = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Message: ")
    while True:
        with open(webhook_file, 'r') as file:
            webhook_urls = file.readlines()

        message_to_send = message

        threads = []

        for url in webhook_urls:
            frequency = 1
            url = url.strip() 
            thread = threading.Thread(target=send_discord_message, args=(url, message_to_send, frequency))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()
               
def Webhook_tool():
    new_title("Webhook Tool discord.gg/nexustools")
    clear()
    print(banner)
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}1{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Spammer{Fore.LIGHTMAGENTA_EX}]")
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}2{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Deleter{Fore.LIGHTMAGENTA_EX}]")
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}3{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Send Message{Fore.LIGHTMAGENTA_EX}]")
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}4{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Check Webhook{Fore.LIGHTMAGENTA_EX}]")
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}5{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Send With Multiple Webhooks{Fore.LIGHTMAGENTA_EX}]")
    print("                                             ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}0{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Exit{Fore.LIGHTMAGENTA_EX}]")
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
        webhook_spammer_multiple()
    if choice == "0":
        quit1()
    else:
        print("Invalid")
        time.sleep(1)
        Webhook_tool()



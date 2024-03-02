from Helper import *

def clear():
    os.system("cls")

def get_tokens():
    with open("Input/tokens.txt", "r") as file:
        tokens = file.readlines()
        return tokens
    
def get_valid_tokens():
    with open("Output/Valid_Tokens.txt", "r") as file:
        tokens = file.readlines()
        return tokens

    
def new_title(title):
    os.system(f"title {title}")

def temp():
    print("this is a temp function :(")
    time.sleep(1)

def quit1():
    print("returning..")
    time.sleep(1)

lc = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.LIGHTMAGENTA_EX}N{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}"
ld = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.LIGHTMAGENTA_EX}-{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}"

banner = f'''{Fore.LIGHTMAGENTA_EX}
                    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                    ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗█████╗██║   ██║   ██║██║   ██║██║     ███████╗
                    ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                discord.gg/nexus-tools
    '''
from Helper import *
from Helper.Common.utils import *



def formater():
    new_title("Token Formater discord.gg/nexustools")
    count = 0
    tokens = get_tokens()
    new_title("Nexus Token Formater")
    change = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Change current token file? (y/n): ")
    if change == "y":
        with open("Input/tokens.txt", "w") as output_file:
            for token in tokens:
                if ":" in token:
                    tokens = token.strip().split(":")[2:]  
                    new_token = ":".join(tokens) + "\n"  
                    output_file.write(new_token)
                    count += 1
                    print(f"{lc} {Fore.LIGHTBLUE_EX}token={Fore.WHITE}{new_token[:20]}...{Fore.RESET} Formatet!")  
                else:
                    print(f"{lc} {Fore.RED}Skipping token={Fore.WHITE}{token[:20]}...{Fore.RESET} (No colon found)")
                    output_file.write(token)      
    with open("Output/formated_tokens.txt", "w") as output_file:
        for token in tokens:
            if ":" in token:
                tokens = token.strip().split(":")[2:]  
                new_token = ":".join(tokens) + "\n"  
                output_file.write(new_token)
                count += 1
                print(f"{lc} {Fore.LIGHTBLUE_EX}token={Fore.WHITE}{new_token[:20]}...{Fore.RESET} Formatet!")
            else:
                print(f"{lc} {Fore.RED}Skipping token={Fore.WHITE}{token[:20]}...{Fore.RESET} (No colon found)")
                output_file.write(token)
    print(f"{ld} Formatet {Fore.GREEN}{count}{Fore.RESET} Tokens!")
    input("Press Enter To continue...")

from Helper import *
from Helper.Common.utils import *



def remove(input_file, output_file):
    try:
        lines_seen = set()  
        temp_output_file = output_file + ".temp"
    
        with open(input_file, 'r') as file_in:
            for line in file_in:
                line = line.strip()
                lines_seen.add(line)
    
        with open(temp_output_file, 'w') as file_out:
            for line in lines_seen:
                file_out.write(line + '\n')

        os.replace(temp_output_file, output_file)

        print(f"{ld} Duplicates removed successfully!")
        input("Press Enter To continue...")
    except:
        print(f"{lc} Error!")
        time.sleep(1)
        remove_duplicates()

def remove_duplicates():
    new_title("Remove Doubles discord.gg/nexustools")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Use Double Remover on tokens.txt? (y/n) ")
    if choice == "y":
        choice2 = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Rewrite Tokens.txt? (y/n) ")
        if choice2 == "y":
            remove("Input/tokens.txt", "Input/tokens.txt")
        else:
            remove("Input/tokens.txt", "Output/removed_doubles.txt")
    else:
        input_file = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Path to file: ")
        remove(input_file, "Output/removed_doubles.txt")
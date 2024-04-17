from Helper import *
from Helper.Common.utils import *



def clean_folder(folder):
    
    clear()
    count = 0
    try:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"{lc} Deleted file: {file_path}")
                    count += 1
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"{lc} Deleted folder and its contents: {file_path}")
            except Exception as e:
                print(f"{ld} Error deleting {file_path}: ")
    except Exception as e:
        print(f"Error {e}")
    input("Press Enter To continue...")
    Cleaner() 

def clean_up_fivem():
    directory_path = r"FiveM\FiveM.app\data"
    clear()
    try:
        appdata_dir = os.getenv('LOCALAPPDATA')
        if appdata_dir:
            target_dir = os.path.join(appdata_dir, directory_path)
            if os.path.exists(target_dir):
                os.chdir(target_dir)
                deleted_files = clean_folder(target_dir)
                if deleted_files == 0:
                    print(f"{ld} fivem is clean")
                    input("Press Enter To continue...")
                    Cleaner()
            else:
                print(ld + "fivem data not found..")
                input("Press Enter To continue...")
                Cleaner()
        else:
            print(ld + "localappdata not found..")
            input("Press Enter To continue...")
            Cleaner()
    except Exception as e:
        print(f"{e} An error occurred: {str(e)}")
        input("Press Enter To continue...")
        Cleaner()

# Discord: sushimampfer Helped Me alot making these fuctions <3
def chrome_history():
    clear()
    try:
        os.remove(os.path.join(os.getenv('LOCALAPPDATA'), "Google\\Chrome\\User Data\\Default\\History"))
        os.remove(os.path.join(os.getenv('LOCALAPPDATA'), "Google\\Chrome\\User Data\\Default\\History-Journal"))
        print(f"{lc} Deleted Browser History")
    except FileNotFoundError:
        print(f"{lc} Browser History Already Deleted")
    input("Press Enter To continue...")
    Cleaner()
    
def chrome_downloads():
    clear()
    try:
        os.remove(os.path.join(os.getenv('LOCALAPPDATA'), "Google\\Chrome\\User Data\\Default\\DownloadMetadata"))
        print(f"{lc} Deleted Download History")
    except FileNotFoundError:
        print(f"{lc} Browser Download Already Deleted")
    input("Press Enter To continue...")
    Cleaner()

# Discord: sushimampfer Helped Me alot making these fuctions <3

def organize(folder_path):
    categories = {
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Music": [".mp3", ".wav", ".flac", ".aac"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Executables": [".exe", ".msi"],
        "Others": [],
    }

    for category in categories:
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1]
            file_type = "Others"
            for category, extensions in categories.items():
                if file_extension.lower() in extensions:
                    file_type = category
                    break
            new_file_path = os.path.join(folder_path, file_type, file_name)
            shutil.move(file_path, new_file_path)
            print(f"Moved {file_name} to {file_type} folder")
    
    input("Press Enter To continue...")
    Cleaner()

def Cleaner():
    new_title("Pc Cleaner discord.gg/nexustools")
    clear()
    print(banner)
    print(f"{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}] Clean Temp")
    print(f"[{Fore.MAGENTA}2{Fore.RESET}] Clean Fivem")
    print(f"[{Fore.MAGENTA}3{Fore.RESET}] Clean Recent")
    print(f"[{Fore.MAGENTA}4{Fore.RESET}] Clean Crashdump")
    print(f"[{Fore.MAGENTA}5{Fore.RESET}] Clean Browser History")
    print(f"[{Fore.MAGENTA}6{Fore.RESET}] Clean Browser Downloads")
    print(f"[{Fore.MAGENTA}7{Fore.RESET}] Clean Desktop")
    print(f"[{Fore.MAGENTA}8{Fore.RESET}] Clean Donwloads")
    print(f"[{Fore.MAGENTA}0{Fore.RESET}] Exit")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    if choice == "1":
        folder = tempfile.gettempdir()
        clean_folder(folder)
    elif choice == "2":
        clean_up_fivem()
    elif choice == "3":
        folder =os.path.join(os.path.expanduser("~"), "Recent")
        clean_folder(folder)
    elif choice == "4":
        folder = os.path.join(os.getenv('LOCALAPPDATA'), 'CrashDumps')
        clean_folder(folder)
    elif choice == "5":
        chrome_history()
    elif choice == "6":
        chrome_downloads()
    elif choice == "7":
        downloads_folder = os.path.expanduser("~/Downloads")  
        organize(downloads_folder)
    elif choice == "8":
        desktop = downloads_folder = os.path.expanduser("~/Desktop")  
        organize(desktop)
    elif choice == "0":
        quit1()
    else:
        Cleaner()
    
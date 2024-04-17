from Helper import *
from Helper.Common.utils import *

def check_serials():
    new_title("Serial Checker discord.gg/nexustools")
    os.system("mode con cols=130 lines=31")
    print("Mainboard")
    os.system("wmic baseboard get serialnumber")
    print("Cpu")
    os.system("wmic cpu get processorid")
    print("Disk")
    os.system("wmic diskdrive get serialnumber")
    print("Bios")
    os.system("wmic bios get serialnumber")
    input("Press Enter To continue...")
    os.system("mode con cols=130 lines=24")
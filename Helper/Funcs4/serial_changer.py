from Helper import *
from Helper.Common.utils import *

def serial_changer():
    print(f"{lc} Changning Serials..")
    new_serial = ''.join(random.choices(string.digits, k=16))
    os.system(f"Helper\Plugs\SerialPlugs\AMIDEWINx64.exe /bs {new_serial}")
    input(f"{lc} Done!")
    input("Press Enter To continue...")
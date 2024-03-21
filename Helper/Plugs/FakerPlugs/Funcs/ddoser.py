from Helper import *
from Helper.Common.utils import *

class ddos:
    def fake_ddoser(target_ip):
        while True:
            num_packets = random.randint(114000, 250000)
            payload = bytearray(random.getrandbits(8) for _ in range(16))
            print(f"{lc} Sending {Fore.GREEN}{num_packets}{Fore.RESET} packets to {Fore.GREEN}{target_ip}{Fore.RESET} Payload: {Fore.LIGHTBLACK_EX}({payload.hex()}){Fore.RESET}")
            time.sleep(0.7)
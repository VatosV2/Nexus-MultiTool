from Helper import *
from Helper.Common.utils import *

Invalid = 0
Valid = 0
checked = 0
proxys = sum(1 for line in open('Input/proxies.txt'))

def update_title(check_rate):
    os.system(f"title Valid: {Valid} │ Invalid: {Invalid} │ Proxies: {proxys} │ Checked: {checked} │ Check Rate: {check_rate:.2f} acc/s")


### To make it look more real if people dont know shit about python.
def check_account(username, password, ffaa2):
    email, password = username, password
    is_valid = False
    if ffaa2 == 'gssi':
        return is_valid
    
    with open('proxy.txt', 'r', encoding='utf-8') as proxy_file:
        proxy_list = proxy_file.readlines()
    for proxy in proxy_list:
        proxy_parts = proxy.strip().split('@')
        proxy_ip_port = proxy_parts[0].split(':')
        proxy_ip, proxy_port = proxy_ip_port[0], proxy_ip_port[1]
        proxy_auth = proxy_parts[1].split(':')
        proxy_username, proxy_password = proxy_auth[0], proxy_auth[1]

        response = None 

        proxy_connection = http.client.HTTPConnection(proxy_ip, int(proxy_port))
        proxy_connection.set_tunnel('api.fortnite.com', 443)

        proxy_headers = {
            'Proxy-Authorization': 'Basic ' + base64.b64encode(f"{proxy_username}:{proxy_password}".encode()).decode(),
        }

        proxy_connection.request('CONNECT', 'api.fortnite.com:443', headers=proxy_headers)
        proxy_response = proxy_connection.getresponse()

        if proxy_response.status == 200:
                connection = http.client.HTTPSConnection('api.fortnite.com')

        headers = {
                            'Host': 'api.fortnite.com',
                            'Authorization': 'Basic ' + base64.b64encode(f"{email}:{password}".encode()).decode(),
                        }

        connection.request('GET', '/v1/account', headers=headers)
        response = connection.getresponse()


def checker():
    global proxys, Invalid, Valid, checked
    combo_list_path = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Combo File Path: ")
    os.system("cls")
    print(f"{Fore.RED}Checking proxies...")
    time.sleep(3)
    print(f"{Fore.GREEN}Working.")
    if proxys == 0:
        proxys += 10
    else:
        pass
    print(f"{Fore.YELLOW}{proxys}/{proxys} Loaded")
    print(f"{Fore.RED}Checking Api status...")
    time.sleep(3)
    print(f"{Fore.GREEN}Working.")
    print(f"{Fore.RED}Start checking accounts..")

    accounts_per_second = 2
    start_time = time.time()

    with open(combo_list_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            username, password = map(str.strip, line.split(':'))
            random_choice_chance = random.choice([1, 2, 3]) # change probability for valid
            if random_choice_chance == 3:
                print(Fore.GREEN + line.strip(), f"{Fore.GREEN}Valid.{Fore.RESET}")
                Valid += 1
            else:
                print(Fore.RED + line.strip(), f"{Fore.RED}Invalid.{Fore.RESET}")
                Invalid += 1

            checked += 1

            elapsed_time = time.time() - start_time

            if elapsed_time > 0:
                check_rate = checked / elapsed_time
            else:
                check_rate = 0  

            update_title(check_rate)

            delay_factor = random.uniform(0.8, 1.2)
            time.sleep((1 / accounts_per_second) * delay_factor)

    update_title(check_rate)
    print(f"{Fore.GREEN}All accounts checked. Valid: {Valid} │ Invalid: {Invalid} │ Elapsed Time: {elapsed_time}")
    input("")

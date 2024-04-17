from Helper import *
from Helper.Common.utils import *


useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
try:
    build_num = int(httpx.get("https://raw.githubusercontent.com/EffeDiscord/discord-api/main/fetch").json()['client_build_number'])
except Exception as e:
    build_num = 201211

config = load_config()
domains = ["outlook.com", "hotmail.com"]
_Api_keys = config['Api_keys']
api_key = _Api_keys['mail_verifier_api']

claimed_count = 0  
verified_count = 0 
error_count = 0

use_proxies = False
Proxie_file = ""



def remove(content, filename):
    lock = threading.Lock()

    with lock:
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines = [line for line in lines if content not in line]
        with open(filename, 'w') as file:
            file.writelines(lines)
            
            
def write(content, filename):
    file_lock = threading.Lock()
    with file_lock:
        with open(filename, 'a') as file:
            file.write(f'{content}\n')


def get_mail():
    mail_type = random.choice(domains)
    url = f'https://api.kopeechka.store/mailbox-get-email?api=2.0&site=discord.com&sender=discord®ex=&mail_type={mail_type}&token={api_key}&soft=99'
    resp = requests.get(url)
    if 'OK' in resp.text:
        return resp.json()['mail'], resp.json()['id']
    elif 'ERROR' in resp.text:
        if resp.json()['value'] == 'OUT_OF_STOCK':
            print(f'{ld} Email is out of stock! Saved as unclaimed.')
        if resp.json()['value'] == 'BAD_BALANCE':
            print(f'{ld} Not enough balance on kopeechka anymore! Saved as unclaimed.')
            
    return None, None


def cancel_mail(mail_id):
    url = f'https://api.kopeechka.store/mailbox-cancel?id={mail_id}&token={api_key}&api=2.0'
    resp = requests.get(url)
    

def get_code(mail_id):
    tries = 0
    while tries < 600:
        time.sleep(1)
        link = requests.get(f"http://api.kopeechka.store/mailbox-get-message?full=$FULL&id={mail_id}&token={api_key}&api=2.0").json()['value']
        if link != 'WAIT_LINK':
            cancel_mail(mail_id)
            link.replace('\\', '')
            break
        
    else:
        cancel_mail(mail_id)
        return False

    verify_token = requests.get(link).url.split('#token=')[1]
    return verify_token

def generate_cookie(session):
    for i in range(1,4):
        try:
            url = "https://discord.com/app"
            resp = session.get(url)
            cookieJar = resp.cookies
            cookies = ""
            for cookie in cookieJar:
                
                cookies = cookies + cookie.name + "=" + cookie.value  + ";"
                
            return cookies
        
        except Exception as e:
            print(e)
            print(f"{ld} Error getting cookies, retrying..")
            continue
        
    print(f"{ld} Failed to get cookies.")
    
    
def build_xsuper():
     
    l = {
    
        "os": 'Windows',
        "browser": 'Chrome',
        "device": "",
        "system_locale": 'en-US',
        "browser_user_agent": useragent,
        "browser_version": '114.0.0.0',
        "os_version": "10",
        "referrer": "https://discord.com",
        "referring_domain": "discord.com",
        "referrer_current": "https://discord.com",
        "referring_domain_current": "discord.com",
        "release_channel": "stable",
        "client_build_number": build_num,
        "client_event_source": None
        
        }
     
    p = json.dumps(l, separators=(',', ':'))
    return [base64.b64encode(p.encode("utf-8")).decode(), 'dHJ5OgogICAgZm9yIGkgaW4gcmFuZ2UoMTApOgogICAgICAgIHByaW50KCdJZiB5b3UgYm91Z2h0IHRoaXMgeW91IGdvdCBzY2FtbWVkIHwgaHR0cHM6Ly9naXRodWIuY29tL1BpeGVucy9Ub2tlbi1NYWlsLVZlcmlmaWVyJykKICAgIHRpbWUuc2xlZXAoMykKICAgIG9zLnN5c3RlbSgnY2xzJyBpZiBvcy5uYW1lID09ICdudCcgZWxzZSAnY2xlYXInKQpleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICBwcmludChlKQ==']

class vars:
    fingerprint_fetch_status = 0

def generate_session(token):
    session = tls_client.Session(client_identifier='chrome114', random_tls_extension_order=True)
    if use_proxies == True:
        session.proxies = "http://" + GetFormattedProxy(Proxie_file)
    xsuper = build_xsuper()
    headers = {
        "accept": "*/*",
        "accept-language": f"en-US;q=0.5",
        "authorization": token,
        "content-type": "application/json",
        "cookie": '',
        "origin": "https://discord.com",
        "referer": "https://discord.com/channels/@me",
        "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": useragent,
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": 'en-US',
        "x-super-properties": xsuper[0]
    }

    if vars.fingerprint_fetch_status == 0:
        vars.fingerprint_fetch_status += 1
        
    session.headers = headers
    cookie = generate_cookie(session)
    session.headers['cookie'] = cookie + f'locale=en-US'
    return session

def claim(old_fulltoken):
    global claimed_count, error_count
    for i in range(1,4):
        
        token = old_fulltoken.split(':')[-1]
        if ':' in old_fulltoken:
            password = old_fulltoken.split(':')[1]
        else:
            password = generate_password()
            
        mail, mail_id = get_mail()
        if mail == None:
            return
        
        try:
            payload = {
                'email': mail,
                'password': password
            }
            session = generate_session(token)
            resp = session.patch('https://discord.com/api/v9/users/@me', json = payload)
            if resp.status_code == 200:
                new_fulltoken = f"{mail}:{password}:{resp.json()['token']}"
                remove(old_fulltoken, "Input/tokens.txt")
                print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CLAIMED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
                claimed_count += 1 
                write(new_fulltoken, "Output/EmailVerifier/claimed.txt")
                print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}VERIFYING{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")
                return verify_token(session, old_fulltoken, new_fulltoken, mail_id)
            else:
                print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}FAILED TO CLAIM{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
                error_count += 1
                cancel_mail(mail_id)
                remove(old_fulltoken, "Input/tokens.txt")
                return
            
        except Exception as e: 
            print(e)
        
    print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}FAILED TO CLAIM{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
    error_count += 1
    cancel_mail(mail_id)
    token11 = new_fulltoken.split(':')[-1]
    return token11
    
    
def verify_token(session, old_fulltoken, new_fulltoken, mail_id):
    global verified_count, error_count
    for i in range(1,4):
        token = new_fulltoken.split(':')[-1]
        mail = new_fulltoken.split(':')[0]
        password = new_fulltoken.split(':')[1]
        session.headers['authorization'] = token
        session.headers['referer'] = 'https://discord.com/verify'
        verify_token = get_code(mail_id)
        if verify_token == False:
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}FAILED TO GET VERIFICATION CODE{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            return token
        try:
            payload = {
                'captcha_key': None, 
                'token': verify_token
            }
            
            resp = session.post('https://discord.com/api/v9/auth/verify', json = payload)
            if resp.status_code == 200:
                verified_token = resp.json()['token']
                verified_fulltoken = f'{mail}:{password}:{verified_token}'
                print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}VERIFIED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
                verified_count += 1
                remove(new_fulltoken, 'Output/EmailVerifier/claimed.txt')
                write(verified_fulltoken, 'Output/EmailVerifier/email_verified_tokens.txt')
                return verified_token
            else:
                print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}FAILED TO VERIFIE{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
                error_count += 1
                return token
            
        except Exception as e: 
            continue
    
    print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}FAILED TO VERIFIE{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
    error_count += 1
    return token

with open("Input/tokens.txt", "r") as file:
    lines = file.readlines()

def process_tokens(start, end):
    for i in range(start, end):
        token = lines[i].strip()
        claim(token)

def main():
    num_threads = 20
    chunk_size = len(lines) // num_threads
    
    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(lines)
        
        thread = threading.Thread(target=process_tokens, args=(start, end))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    print(f"{ld} Claimed Tokens: {Fore.GREEN}{claimed_count}{Fore.RESET}")
    print(f"{ld} Verified Tokens: {Fore.GREEN}{verified_count}{Fore.RESET}")
    print(f"{ld} Failed Token: {Fore.GREEN}{error_count}{Fore.RESET}")
    input("Press Enter To continue...")
    quit1()

def update_console_title():
    while True:
        resp = httpx.get(f"http://api.kopeechka.store/user-balance?token={_Api_keys['mail_verifier_api']}&api=2.0")
        balance = resp.json()['balance']
        title = f"Nexus Mail Verifier Claims: {claimed_count} | Verifies: {verified_count} | Errors: {error_count} | Balance: {balance} RUB"

def TokenMailverifier():
    new_title("Mail Verifier discord.gg/nexustools")
    os.system("cls")
    print(Fore.LIGHTMAGENTA_EX + '''
                    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                    ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗█████╗██║   ██║   ██║██║   ██║██║     ███████╗
                    ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                discord.gg/nexus-tools
    ''')
    proxies = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Use Proxies? (y/n): ")
    if proxies == "y":
        print(f"{lc} {Fore.GREEN}Using Proxies!{Fore.RESET}")
        use_proxies = True
        proxie_file_ask = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Use Input/proxies.txt? (y/n): ")
        if proxie_file_ask == "y":
            Proxie_file = "Input/proxies.txt"
        else:
            proxie_file_path = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Drag and Drop Proxie File: ")
            Proxie_file = proxie_file_path
    else:
        print(f"{lc} {Fore.RED}Not Using Proxies{Fore.RESET}")
        use_proxies = False
    if not _Api_keys['mail_verifier_api']:
        print(f'{ld} Input your kopeechka API key in the config.')
    resp = httpx.get(f"http://api.kopeechka.store/user-balance?token={_Api_keys['mail_verifier_api']}&api=2.0")
    if 'OK' not in resp.text:
        print(f'{ld} Error getting kopeechka balance: ' + resp.json()['value'])
        time.sleep(3)
        quit()
    balance = resp.json()['balance']
    update_thread = threading.Thread(target=update_console_title)
    update_thread.daemon = True  
    update_thread.start()
    main()

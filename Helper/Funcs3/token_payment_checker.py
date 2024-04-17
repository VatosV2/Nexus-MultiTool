from Helper import *
from Helper.Common.utils import *

ptokens = []

def check_payment_methods(token):
    headers = {
        'Authorization': token
    }

    response = requests.get('https://discord.com/api/v9/users/@me/billing/payment-sources', headers=headers)

    if response.status_code == 200:
        payment_methods = response.json()
        if payment_methods:
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Payment methods found:")
            ptokens.append(token)
            for method in payment_methods:
                print(f"{lc} - {method['brand']} ending in {method['last_4']}")
        else:
            print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} No payment methods found.")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Failed to fetch payment methods. Make sure the token is correct.")


def check_payments():
    new_title("Token Payment Checker discord.gg/nexustools")
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    threads = []
    for token in tokens:
        token = token.strip()
        thread = threading.Thread(target=check_payment_methods, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    with open("Output/Payment_tokens/tokens.txt", 'w') as file:
        for full_token in ptokens:
            file.write(f"{full_token}\n")
    print(f"{lc} Tokens with payment saved in Output/Payment_tokens/tokens.txt !")
    input("Press Enter To continue...")
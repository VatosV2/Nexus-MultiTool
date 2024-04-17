from Helper import *
from Helper.Common.utils import *


def token_login():
    new_title("Token Login discord.gg/nexustools")
    token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token To Login: ")
    option = uc.ChromeOptions()
    driver = uc.Chrome(options=option)
    driver.get("https://discord.com/channels/@me")
    script = """
    function login(token) {
    setInterval(() => {
        if (document.body) {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`;
            clearInterval();
        }
    }, 50);
    setTimeout(() => {
        location.reload();
    }, 2500);
    }
    """

    driver.execute_script(script + f'\nlogin("{token}")')
    input("")

from Helper import *
from Helper.Common.utils import *

class gen:
    def generate_email():
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))
        return f"{email}@gmail.com"

    def generate_password():
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=14))
        return password

    def generate_token():
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
        secret = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        secret2 = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        return f"MTEx{secret2}.{secret}.{token}"
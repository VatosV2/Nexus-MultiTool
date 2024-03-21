from Helper import *
from Helper.Common.utils import *

class person:
    def create_fake_profile():
        fake = Faker()
    
        name = fake.name()
        address = fake.address()
        email = fake.email()
        phone_number = fake.phone_number()
        job = fake.job()
        company = fake.company()
        ssn = fake.ssn()
        credit_card_number = fake.credit_card_number()
        username = fake.user_name()

        print("Name:", name)
        print("Address:", address)
        print("Email:", email)
        print("Phone Number:", phone_number)
        print("Job:", job)
        print("Company:", company)
        print("Social Security Number:", ssn)
        print("Credit Card Number:", credit_card_number)
        print("Username:", username)
        input()


import bank
import utils

##FOR REGISTERING A NEW USER
def get_age():
    while True:
        try:    
            user_input = int(input("Age: "))
            if utils.age_verification(user_input):
                age = user_input
                return age
            else:
                return False
        except ValueError:
            print("Age can only be whole numbers.")
        except KeyboardInterrupt:
            return

def get_email():
    while True:
        try:
            user_input = input("Valid Email: ")
            if utils.email_validation(user_input):
                email = user_input
                return email
            else:
                print("This email is invalid")
        except KeyboardInterrupt:
            return

def get_contact():
    while True:
        try:
            user_input = input("Valid Contact line: ")
            if utils.validate_contact(user_input):
                contact = user_input
                return contact
            else:
                print("This contact is invalid.")
        except KeyboardInterrupt:
            return

def get_pin():
    while True:
        try:
            user_input = input("Create a 4-Digit pin: ")
            if utils.pin_len_check(user_input):
                raw_pin = user_input
                return raw_pin
        except KeyboardInterrupt:
            return

def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            return amount
        except ValueError:
            print("Invalid input.")
        except KeyboardInterrupt:
            return


def collect_registration_data():
    age = get_age()
    if age:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = get_email()
        if email:
            contact = get_contact()
            if contact:
                raw_pin = get_pin()
                if raw_pin:
                    return bank.register_user(first_name, last_name, age, email, contact, raw_pin)

    else:
        print("You cannot open an account at this age.\n")
        return None


##LOGIN FOR EXISTING USER
def collect_login_data():
    acct_num = input("Enter account number: ")
    raw_pin = input("Enter your 4_Digit pin: ")
    user_session = bank.authenticate_user(acct_num, raw_pin)
    if not user_session:
        return None
    else:    
        return user_session
import utils
import storage
import accounts

def register_user(first_name, last_name, age, email, contact, raw_pin):
    hashed_pin = utils.hash_pin(raw_pin)
    acct_num = utils.generate_account_number()
    balance = 0.00

    info_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email,
        "contact": contact
    }

    storage.save_account_data(acct_num, info_dict, hashed_pin, balance)
    return acct_num

def authenticate_user(acct_num, raw_pin):
    if not storage.account_exists(acct_num):
        return None

    user_data = storage.read_account_data(acct_num)
    if not user_data:
        return None
    else:
        hashed_pin = utils.hash_pin(raw_pin)
        if hashed_pin == user_data["hashed_pin"]:
            user = accounts.BankAccount(
                user_data["first_name"],
                user_data["last_name"],
                user_data["age"],
                user_data["email"],
                user_data["contact"],
                user_data["hashed_pin"],
                acct_num,
                user_data["balance"]
            )
            return user
        else:
            return None
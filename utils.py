from datetime import datetime, timezone, timedelta
import hashlib
import random
import storage

def age_verification(age):
    if age >= 18 and age <= 120:
        return True
    else:
        return False

def hash_pin(user_key):
    #user_key: str
    return hashlib.sha256(user_key.encode()).hexdigest()

def pin_len_check(user_key):
    #user_key: str
    if len(user_key) == 4 and user_key.isdigit():
        return True
    else:
        return False

def email_validation(user_email):
    #user_email: str
    if user_email.count("@") == 1:
        at_index = user_email.index("@")
        if at_index > 0 and at_index < len(user_email) - 3:
            return "." in user_email[at_index:]
    return False

def validate_contact(contact_info):
    #contact_info: str
    return contact_info.isdigit() and len(contact_info) in (10,11)

def generate_account_number():
    while True:
        acct = "".join(str(random.randint(0,9)) for _ in range(10))
        if not storage.account_exists(acct):
            return acct

def get_timestamp():
    west_african_time = timezone(timedelta(hours=1))# WAT is GMT+1
    now = datetime.now(west_african_time)
    formatted_time = now.strftime("%Y-%b-%d  %I:%M:%S %p %Z")
    return formatted_time

def generate_transaction_id(acct_num):
    while True:
        id = "".join(str(random.randint(0,9)) for _ in range(6))
        transact_id = f"TXN-{id}"
        record_check = storage.read_transaction_records(acct_num)
        if not record_check:
            return transact_id
        if not any(transact_id in records for records in record_check):
            return transact_id
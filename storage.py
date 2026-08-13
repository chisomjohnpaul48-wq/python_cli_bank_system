import os
#PermissionError: OS blocks python from creating a folder or reading a file.
#OSError: A general fallback for disk or file_system issues.


def init_storage():
    # CREATES THE BASE IF IT DOESN'T EXIST
    try:
        os.makedirs("Container/accounts", exist_ok=True)
        return True
    except PermissionError:
        print("Error: Permission denied. Cannot create storage directory.")
        return False
    except OSError as e:
        print(f"Error initializing storage: {e}")
        return False

def account_exists(acct_num):
    # acct_num: str
    # CHECKS IF A DIRECTORY FOR THE GIVEN ACCOUNT NUMBER EXISTS.
    try:
        account_dir = os.path.join("Container", "accounts", acct_num)
        return os.path.exists(account_dir)
    except OSError as e:
        print(f"Error checking account existence: {e}")
        return False

def save_account_data(acct_num, info_dict, hashed_pin, balance):
    try:
        #Confirm directory exists
        account_dir = os.path.join("Container", "accounts", acct_num)
        os.makedirs(account_dir, exist_ok=True)

        #SAVING FILES
        account_dir_info = os.path.join("Container", "accounts", acct_num, "info.txt")
        with open(account_dir_info, "w") as file:
            for key, value in info_dict.items():
                file.write(f"{key}={value}\n")

        account_dir_security = os.path.join("Container", "accounts", acct_num, "security.txt")
        with open(account_dir_security, "w") as file:
            file.write(hashed_pin)

        account_dir_balance = os.path.join("Container", "accounts", acct_num, "balance.txt")
        with open(account_dir_balance, "w") as file:
            file.write(str(balance))

        return True
    except PermissionError:
        print("Error: Permission denied. Cannot create storage directory.")
        return False
    except OSError as e:
        print(f"Error initializing storage: {e}")
        return False


def read_account_data(acct_num):
    if account_exists(acct_num):
        try:
            data= {}
            account_dir_info = os.path.join("Container", "accounts", acct_num, "info.txt")
            with open(account_dir_info, "r") as file:
                for line in file.readlines():
                    key, value = line.strip().split("=")
                    data[key] = value
                    
            account_dir_security = os.path.join("Container", "accounts", acct_num, "security.txt")
            with open(account_dir_security, "r") as file:
                data["hashed_pin"] = file.read()

            account_dir_balance = os.path.join("Container", "accounts", acct_num, "balance.txt")
            with open(account_dir_balance, "r") as file:
                acct_bal = float(file.read())
                data["balance"] = acct_bal

            return data
        except ValueError:
            return None
        except FileNotFoundError:
            print("Error: File not found.")
            return None
        except PermissionError:
            print("Error: Permission denied. Cannot create storage directory.")
            return None
        except OSError as e:
            print(f"Error initializing storage: {e}")
            return None              
    else:
        return None


def update_balance(acct_num, new_balance):
    #new_balance: str
    if account_exists(acct_num):
        try:
            account_dir_balance = os.path.join("Container", "accounts", acct_num, "balance.txt")
            with open(account_dir_balance, "w") as file:
                file.write(str(new_balance))
                return True
        except FileNotFoundError:
            print("Error: File not found.")
            return False
        except OSError as e:
            print(f"Error initializing storage: {e}")
            return False
    else:
        return None
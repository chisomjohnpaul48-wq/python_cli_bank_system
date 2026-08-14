import cli_handlers
import storage
import transactions


storage.init_storage()
print("==== WELCOME TO ME BANK ====")
while True:
    print("""[1] Register
[2] Login
[3] Exit
Enter action""")

    try:
        user_input = input("> ")

        if user_input == "1":
            ##CREATING NEW ACCOUNT
            print("Welcome new user\nPlease fill in the following details.")
            new_account = cli_handlers.collect_registration_data()
            if new_account:
                print(f"Welcome new user.\nYour account number is {new_account}\n")


        elif user_input == "2":
            ##LOGIN EXISTINNG ACCOUNT
            login = cli_handlers.collect_login_data()
            if not login:
                print("Invalid account number or pin.")
            else:
                print(f"Welcome {login.first_name}")
                while True:
                    print("[1] Check Balance: :[2] Deposit: :[3] Withdraw: :[4] Transaction History: :[5] Logout")
                    user_input2 = input("> ")
                    if user_input2 == "1":
                        print(f"Your account balance is {login.check_balance()}")

                    elif user_input2 == "2":
                        amount_to_deposit = cli_handlers.get_amount()
                        deposit = login.deposit(amount_to_deposit)
                        if deposit:
                            print("Transaction successful.")
                        else:
                            print("Transaction failed.")

                    elif user_input2 == "3":
                        amount_to_withdraw = cli_handlers.get_amount()
                        withdraw = login.withdrawal(amount_to_withdraw)
                        if withdraw:
                            print("Transaction successful.")
                        else:
                            print("Transaction failed.")

                    elif user_input2 == "4":
                        txn_history = login.read_txns()
                        if txn_history:
                            print("===== TRANSACTION HISTORY =====")
                            for transaction in txn_history:
                                print(transaction, end="")
                        else:
                            print("<Empty>: Nothing to see here.")

                    elif user_input2 == "5":
                        print(f"Logged out {login.first_name}")
                        break
                    else: 
                        print("Invalid input.")
                

        elif user_input == "3":
            ##EXIT
            print("Thank you for banking with us.")
            break

        else:
            ##FALLBACK
            print("Invalid input")


    except KeyboardInterrupt:
        print("Operation Cancelled.")
        break
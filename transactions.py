import utils
import storage

##TRANSACTION INFO
def log_transaction(acct_num, txn_type, amount, current_balance):
    if not storage.account_exists(acct_num):
        return None
    else:
        txn_id = utils.generate_transaction_id(acct_num)
        time = utils.get_timestamp()
        transaction_line = f"{txn_id} | Transaction type: {txn_type} | Amount: {amount} | Balance: {current_balance} | Time: {time}"
        upload_data = storage.append_transaction_records(acct_num, transaction_line)
        if upload_data:
            return True
        else:
            return None

def display_txn_history(acct_num):
    if not storage.account_exists(acct_num):
        return None
    else:
        txn_record = storage.read_transaction_records(acct_num)
        if not txn_record:
            return None
        else:
            return txn_record
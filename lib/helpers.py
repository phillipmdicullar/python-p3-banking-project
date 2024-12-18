from db.models import Account, session

def create_account(account_number, account_holder_name, initial_deposit=0):
    account = Account(account_number=account_number, account_holder_name=account_holder_name, balance=initial_deposit)
    session.add(account)
    session.commit()
    print(f"Account created successfully for {account_holder_name} with account number {account_number}.")

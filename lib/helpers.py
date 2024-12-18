from db.models import Account, session

def create_account(account_number, account_holder_name, initial_deposit=0):
    account = Account(account_number=account_number, account_holder_name=account_holder_name, balance=initial_deposit)
    session.add(account)
    session.commit()
    print(f"Account created successfully for {account_holder_name} with account number {account_number}.")
def deposit_money(account_number, amount):
    account = session.query(Account).filter(Account.account_number == account_number).first()
    if account:
        account.balance += amount
        session.commit()
        session.close()
        print(f"{amount} deposited successfully to account number {account_number}.")
    else:
        print("Account not found.")
def withdraw_money(account_number, amount):
    account = session.query(Account).filter(Account.account_number == account_number).first()
    if account:
        if account.balance >= amount:
            account.balance -= amount
            session.commit()
            print(f"{amount} withdrawn successfully from account number {account_number}.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")
def check_balance(account_number):
    account = session.query(Account).filter(Account.account_number == account_number).first()
    if account:
        print(f"Account Balance for {account_number}: {account.balance}")
    else:
        print("Account not found.")
def display_all_accounts():
    accounts = session.query(Account).all()
    if accounts:
        for account in accounts:
            print(f"Account Number: {account.account_number}, Account Holder: {account.account_holder_name}, Balance: {account.balance}")
    else:
        print("No accounts found.")
def authenticate_user(username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        return {"username": user.username, "role": user.role}
    return None

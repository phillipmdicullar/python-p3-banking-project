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
# List to store user data
users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "user1", "password": "password1", "role": "customer"},
    {"username": "user2", "password": "password2", "role": "customer"},
]

def authenticate_user(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return {"username": user["username"], "role": user["role"]}
    return None

def signup_user(username, password, role="customer"):
    for user in users:
        if user["username"] == username:
            return False  # User already exists
    users.append({"username": username, "password": password, "role": role})
    return True

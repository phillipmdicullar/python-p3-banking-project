from models import Account, session
def seed_accounts():
    account1 = Account(account_number=1234, account_holder_name="Alice", balance=500)
    session.add(account1)
    session.commit()

    print("Initial accounts seeded.")
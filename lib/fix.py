from helpers import authenticate_user, signup_user
from animations import typing_effect

def login():
    while True:
        print("--- Admin-Login-Panel ---")
        typing_effect("Welcome to Python Bank! Please log in.")
        user = authenticate_user(username, password)
        if user:
            typing_effect(f"Login successful! Welcome, {user['username']}.")
            return user
            show_menu()
        else:
            print("Invalid username or password. Please try again.")

def signup():
    print("--- Signup Panel ---")
    typing_effect("Create a new account.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if signup_user(username, password):
        typing_effect(f"Account created successfully! Welcome, {username}.")
        show_menu()
    else:
        print("Username already exists. Please try again.")

def main():
    while True:
        print("--- Welcome to Python Bank ---")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            current_user = login()
            if current_user:
                # Show the banking menu based on role
                print(f"Hello, {current_user['username']}! You are logged in as {current_user['role']}.")
                # Add functionality for banking operations here
        elif choice == '2':
            signup()
        elif choice == '3':
            print("Thank you for using Python Bank!")
            break
        else:
            print("Invalid choice. Please try again.")
def show_menu():
    os.system("clear")
    os.system("toilet -f pagga -w $(tput cols) 'CODE [-_-] BANK'")
    print("--- Welcome to (-_-) Bank ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Exit")
def main():
    while True:
        show_logo()
        
        Login()
        
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = int(input("Enter account number: "))
            account_holder_name = input("Enter account holder name: ")
            initial_deposit = float(input("Enter initial deposit (default 0): ") or 0)
            create_account(account_number, account_holder_name, initial_deposit)
            progress_bar("Creating account")
            print("Account created successfully!")



        elif choice == '2':
            account_number = int(input("Enter account number: "))
            deposit_amount = float(input("Enter deposit amount: "))
            deposit_money(account_number, deposit_amount)
            print("Depositing in your your account...")
            loading_spinner()
            print("Deposited successfully!")

        elif choice == '3':
            account_number = int(input("Enter account number: "))
            withdraw_amount = float(input("Enter withdrawal amount: "))
            withdraw_money(account_number, withdraw_amount)

        elif choice == '4':
            account_number = int(input("Enter account number: "))
            print("Checking your balance...")
            loading_spinner()
            check_balance(account_number)


        elif choice == '5':
            loading_spinner()
            display_all_accounts()

        elif choice == '6':
            print("Thank you for using Python Bank")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

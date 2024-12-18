from animations import *
import os
from helpers import create_account,authenticate_user, deposit_money, withdraw_money, check_balance, display_all_accounts
def Login():
    print("--- Admin-Login-Panel ---")
    print("Your default creds is username=admin password=password" )
    print("This is only for simulation")
    Username = input("Enter username: ")
    Password = input("Enter password: ")

    if Username == 'admin' and Password == 'password':
       
        print("Login successful.")
        
        show_menu()
    else:
        print("Invalid credentials.")
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
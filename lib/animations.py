import sys
import time
from colorama import Fore, Style
def loading_spinner(message="Processing"):
    spinner = ['|', '/', '-', '\\']
    for _ in range(10):  # Adjust the range for a longer or shorter animation
        for symbol in spinner:
            sys.stdout.write(f"\r{message}... {symbol}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\rDone!         \n")


def progress_bar(task="Processing", total=30):
    print(task)
    for i in range(total + 1):
        bar = ('#' * i).ljust(total)
        sys.stdout.write(f"\r[{bar}] {i * 100 // total}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print()  # Move to the next line after the progress bar completes

def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after typing
typing_effect("Welcome to Python Bank...")
typing_effect("Let's get started!")
def show_logo():
    logo = """
    ╔══════════════════════════════════════╗
    ║          Welcome to Python Bank      ║
    ║      Your Trusted Financial Partner  ║
    ╚══════════════════════════════════════╝
    """
    print(logo)



def countdown_timer(seconds=3, message="Redirecting to main menu"):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r{message} in {i} seconds...")
        sys.stdout.flush()
        time.sleep(1)
    print("\nDone!")


def show_colored_message():
    print(Fore.GREEN + "Success! Your account has been created." + Style.RESET_ALL)
    print(Fore.RED + "Error: Invalid account number." + Style.RESET_ALL)

def atm_screen(message="Welcome to Python Bank"):
    border = "=" * 30
    print(border)
    print(f"{message.center(30)}")
    print(border)


def money_deposit_animation():
    for i in range(5):
        sys.stdout.write("\r💵💵💵💵💵💵 " * (i + 1))
        sys.stdout.flush()
        time.sleep(0.5)
    print("\nDeposit complete!")

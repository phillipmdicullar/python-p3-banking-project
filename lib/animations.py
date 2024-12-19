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


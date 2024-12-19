# Python CLI Code Bank Project 🌍

## Description

* The Python CLI Banking System is a command-line application designed to simulate basic banking operations such as creating accounts, depositing money, withdrawing money, checking account balances, and displaying all accounts. 
* This project showcases the use of Python fundamentals, SQLAlchemy ORM, and a structured CLI to create a practical solution to real-world banking problems.

## Features
- **Account Management**: Create, retrieve, and manage customer accounts.

### Transactions:

- Deposit money.
- Withdraw money.
- Check account balances.
- **Data Persistence**: Store all account and transaction data in an SQLite database using SQLAlchemy ORM.
-**User-Friendly CLI**: An intuitive command-line interface with animations and visual enhancements.
-**Preloaded Users**: Default accounts for demonstration purposes.
## 🚀 Technologies used
- **Python**: Core programming language.
-**SQLAlchemy**: ORM for managing the SQLite database.
-**SQLite**: Lightweight relational database for data storage.
-**Pipenv**: Virtual environment and dependency manager.
## 🛠️ Project Structure
```
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py         # Main CLI logic
    ├── db
    │   ├── models.py  # Database models
    │   └── seed.py    # Script to seed the database with default data
    ├── debug.py       # Debugging and testing tools
    └── helpers.py     # Utility functions for animations and CLI enhancements
```

## 🖥️ Installation and Setup

### Prerequisites

- **Python 3.8+**
- **Pipenv installed**
- **Linux Os**

### Steps

- Clone the repository:

```git clone https://github.com/phillipmdicullar/python-p3-banking-project```
```cd python-p3-banking-project```

### Install dependencies:

```pipenv install```

### Activate the virtual environment:

```pipenv shell```

### Initialize the database:

```python lib/db/seed.py```

### Run the application:

```python lib/cli.py```


## 🌟 Usage 
- 🔍 Upon running the application you will be presented with a menu. 

```
Welcome to the Python Bank
 1. Create Account
 2. Deposit Money
 3. Withdraw Money
 4. Check Balance
 5. Display All Accounts
 6. Exit
```
### Example

- 🛠️ **Follow the prompts to perform banking operations**:
**Creating an account.**
```
Enter your choice: 1
Enter account number: 1234
Enter account holder name: Beatrice
Enter initial deposit (default 0): 50000
Account created successfully.
```
📦 - **Depositing money**

```
Enter your choice: 2
Enter account number: 1234
Enter deposit amount: 200
200 deposited successfully.
```

## 🚧 Future Enhancements 
* Add multi-user authentication.
* Implement transfer functionality between accounts.
* Introduce a graphical user interface (GUI).
* Add unit tests for core functionalities.

## 👥 Contributers 
1. **Philip Emdokolo** 

## 📝 License This project is licensed under the MIT License 
- see the [LICENSE](LICENSE) file for details. 

   <p align="center"> Made with ❤️ by <a href="https://github.com/phillipmdicullar">Philip Emdokolo🤧</a> </p>


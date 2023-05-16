# Banking System Simulator

This Python program simulates a basic banking system where users can perform various banking operations such as opening an account, closing an account, making deposits, transferring money, and withdrawing money. The program provides a console-based user interface.

## Features

- Account Creation: Users can open a new bank account by providing their name and initial balance. After creating they receive an *account number* back. Each account has its own number, which is used in all other operations.
- Account Closure: Users can close an existing account by specifying the account number.
- Deposit Money: Users can make deposits into their accounts by providing the account number and the deposit amount.
- Money Transfer: Users can transfer money from one account to another by specifying the source account number, destination account number, and the transfer amount.
- Money Withdrawal: Users can withdraw money from their accounts by specifying the account number and the withdrawal amount.
- Main Loop: The program has a main repetition loop that continuously prompts the user to choose an option and perform the desired operation.


## Data Persistence

- Account details, including account holder's name, balance, and account number, are stored in a local JSON file for data persistence. The basic implementation to read and update a JSON file is provided by the `file_helper.py`. Just make sure to create the `.json` file before calling it. Create an issue _(or message me)_ if you are having trouple using it.

## Usage

1. Clone this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Run the program using the following command: `python3 main.py`
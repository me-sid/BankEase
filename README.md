
# BankEase — Python Bank Management System

A simple, menu-driven bank management system built using basic Python programming concepts. BankEase allows users to create bank accounts, log in using a PIN, perform banking operations, and maintain transaction records.

The project uses Python dictionaries for handling account data in memory and JSON for permanent data storage. It is designed to be beginner-friendly, easy to understand, and suitable for academic projects and demonstrations.

## 1. Project Overview

- **Project Name:** BankEase
- **Language:** Python
- **Data Storage:** JSON
- **Application Type:** Console-based, menu-driven application
- **External Libraries:** None
- **Programming Approach:** Procedural programming using functions, dictionaries, lists, loops, and conditional statements.

### Objectives

- Develop a basic banking application using Python.
- Understand how dictionaries store structured data.
- Learn how JSON enables permanent data storage.
- Implement basic banking operations such as deposits, withdrawals, and transfers.
- Apply input validation and conditional logic.
- Organize a program into reusable functions.
- Maintain a transaction history for each account.

## 2. Project Structure

The project consists of the following files:

```text
BankEase/
├── bankease.py
├── accounts.json
└── README.md
```

### `bankease.py`

The main Python program. It contains all application logic, including account creation, login, banking operations, transaction management, input validation, and menu navigation.

### `accounts.json`

Stores account information permanently in JSON format. It is created automatically when the program starts if the file does not already exist.

The file stores account details, PINs, balances, and transaction histories.

### `README.md`

Documents the project, its functionality, implementation, and usage.

**Note:** Keep `accounts.json` in the same working directory from which you run the application. It contains the application's data.

## 3. Features

### 3.1 Account Creation

Users can create a new account by providing:

- Account number
- Full name
- Age
- Phone number
- Address
- Account type: Savings or Current
- Four-digit PIN
- Initial deposit

The application validates the account number, checks for duplicate accounts, validates the phone number and PIN, and ensures the initial deposit is positive.

Once the details are accepted, a new account is added to the accounts dictionary and saved to the JSON file.

### 3.2 Login

Users log in using their account number and PIN.

The application checks whether the account exists and compares the entered PIN with the stored PIN. A maximum of three PIN attempts is allowed per login session.

After successful authentication, the user is taken to the account menu.

### 3.3 Account Details

Users can view their account number, name, age, phone number, address, account type, and current balance.

The PIN is not displayed on the account details screen.

### 3.4 Check Balance

Displays the current balance of the logged-in account.

### 3.5 Deposit Money

Users can deposit a positive amount into their account.

The application adds the amount to the current balance, records the transaction with its date and time, and saves the updated information to the JSON file.

### 3.6 Withdraw Money

Users can withdraw money if they have sufficient funds.

The application checks the requested amount against the available balance. If sufficient funds are available, the balance is reduced, the transaction is recorded, and the updated data is saved.

### 3.7 Transfer Money

Users can transfer money to another existing BankEase account.

The application checks that:

- The receiver account exists.
- The sender is not transferring money to their own account.
- The transfer amount is positive.
- The sender has sufficient funds.

After a successful transfer, the sender's balance decreases and the receiver's balance increases. Both accounts receive a corresponding transaction record.

### 3.8 Transaction History

Displays the transactions associated with the logged-in account.

The history includes account creation, deposits, withdrawals, outgoing transfers, incoming transfers, and PIN changes.

Each transaction includes a date and time.

### 3.9 Change PIN

Users can change their PIN after providing their current PIN.

The application validates the new four-digit PIN, checks that it differs from the current PIN, and asks the user to confirm it. The new PIN is saved to the JSON file.

### 3.10 Close Account

Users can close their account after confirming the operation and entering the correct PIN.

For simplicity, an account can only be closed when its balance is zero.

After closure, the account is removed from the accounts dictionary and the JSON file is updated. The transaction history is removed along with the account.

### 3.11 Logout

Users can log out of their account and return to the main menu without terminating the program.

### 3.12 Exit

Terminates the application. All successful changes have already been saved to the JSON file.

## 4. Application Menus

### Main Menu

```text
====================================
        WELCOME TO BANKEASE
====================================
1. Create Account
2. Login
3. Exit
====================================
```

### Account Menu

```text
====================================
          BANKEASE MENU
====================================
1. Account Details
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Transfer Money
6. Transaction History
7. Change PIN
8. Close Account
9. Logout
====================================
```

The program uses a `while` loop to repeatedly display the menus until the user chooses to exit or log out.

Conditional statements (`if`, `elif`, and `else`) determine which function runs for each menu choice.

## 5. How the Application Works

BankEase follows a simple flow from startup to exit.

```text
                  Start
                    |
                    v
              Load JSON Data
                    |
                    v
                Main Menu
                    |
          +---------+---------+
          |         |         |
          v         v         v
      Create      Login      Exit
      Account       |
                    v
              Verify Account
                    |
                    v
              Account Menu
                    |
          +---------+----------+
          |         |          |
          v         v          v
       Deposit   Withdraw   Transfer
          |         |          |
          +---------+----------+
                    |
                    v
             Update Dictionary
                    |
                    v
               Save to JSON
                    |
                    v
            Continue or Logout
```

### Step 1: Load Account Data

When the application starts, the `main()` function calls `load_data()`.

If `accounts.json` exists, its contents are read and converted into a Python dictionary.

If the file does not exist, an empty JSON file is created and an empty dictionary is returned.

### Step 2: Display the Main Menu

The user chooses to create an account, log in, or exit.

### Step 3: Perform the Selected Operation

Each menu option calls a dedicated function. For example, `deposit()` handles deposits, while `transfer()` handles transfers between accounts.

### Step 4: Update Account Information

The banking functions modify the account dictionary in memory.

### Step 5: Save Changes

After a successful operation that changes stored data, `save_data()` writes the updated dictionary to `accounts.json`.

### Step 6: Continue Using the Application

The user can perform additional operations, log out, or exit the program.

## 6. Data Storage and JSON

One of the main concepts used in BankEase is JSON-based data persistence.

### What Is JSON?

JSON stands for JavaScript Object Notation. It is a text-based format for storing and exchanging structured data.

Python's built-in `json` module provides functions to convert between Python objects and JSON data.

BankEase uses two functions:

- `json.load()` reads JSON data from a file and converts it into Python objects.
- `json.dump()` converts Python objects into JSON format and writes them to a file.

### Example `accounts.json`

```json
{
    "1001": {
        "name": "Siddhartha",
        "age": 18,
        "phone": "9876543210",
        "address": "Vellore",
        "type": "Savings",
        "pin": "1234",
        "balance": 5000.0,
        "transactions": [
            "27-10-2026 10:00:00 - Account created with Rs. 5000.0",
            "27-10-2026 10:10:00 - Deposited Rs. 1000.00"
        ]
    }
}
```

This is an illustrative example. The dates and transaction values depend on actual usage.

### Why Is the Account Number a String?

The account number is collected using `input()`, which returns a string.

Therefore, the account number is used as a dictionary key such as `"1001"` rather than the integer `1001`.

This also preserves leading zeros if an account number contains them.

### Why Is the Account Data a Dictionary of Dictionaries?

The outer dictionary stores accounts, using each account number as its key.

The inner dictionary stores the details of a particular account.

For example:

```python
accounts = {
    "1001": {
        "name": "Siddhartha",
        "balance": 5000.0
    },
    "1002": {
        "name": "Rahul",
        "balance": 3000.0
    }
}
```

To access Siddhartha's balance:

```python
accounts["1001"]["balance"]
```

To access Rahul's name:

```python
accounts["1002"]["name"]
```

This structure makes it easy to retrieve and update account information.

### The `load_data()` Function

```python
def load_data():
    if os.path.exists(ACCOUNTS_FILE):
        try:
            with open(ACCOUNTS_FILE, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            print("Error: accounts.json contains invalid data.")
            print("Please repair the file before running BankEase.")
            raise SystemExit

    else:
        with open(ACCOUNTS_FILE, "w") as file:
            json.dump({}, file, indent=4)

        return {}
```

The function checks whether the file exists.

If it exists, the file is opened in read mode (`"r"`) and its contents are loaded.

If it does not exist, the program creates it and writes an empty dictionary.

The `with` statement automatically closes the file after the operation.

The `try` and `except` block handles invalid JSON syntax.

### The `save_data()` Function

```python
def save_data(accounts):
    with open(ACCOUNTS_FILE, "w") as file:
        json.dump(accounts, file, indent=4)
```

This function writes the current accounts dictionary to the JSON file.

The `"w"` mode opens the file for writing and replaces its existing contents.

The `indent=4` argument formats the JSON using four spaces per indentation level, making the file easier to read.

**Important:** Writing in `"w"` mode replaces the file's previous contents. The updated dictionary must therefore contain all accounts that need to be retained.

### How Data Persistence Works

```text
accounts.json
     |
     | json.load()
     v
Python Dictionary
     |
     | Perform operation
     v
Updated Dictionary
     |
     | json.dump()
     v
Updated accounts.json
```

Unlike a dictionary-only application, JSON storage allows account information to remain available after the program closes and starts again.

## 7. Explanation of Important Functions

| Function | Purpose |
|---|---|
| `main()` | Loads the data and controls the main menu. |
| `load_data()` | Reads account information from JSON. |
| `save_data(accounts)` | Writes account information to JSON. |
| `account_exists()` | Checks whether an account number is present. |
| `is_valid_pin()` | Checks whether a PIN contains four digits. |
| `is_valid_phone()` | Checks whether a phone number contains ten digits. |
| `is_valid_amount()` | Checks whether an entered amount is positive and numeric. |
| `get_amount()` | Repeatedly requests a valid positive amount. |
| `add_transaction()` | Adds a transaction with a timestamp. |
| `create_account()` | Collects details and creates an account. |
| `login()` | Authenticates a user. |
| `account_details()` | Displays account information. |
| `check_balance()` | Displays the current balance. |
| `deposit()` | Adds money to an account. |
| `withdraw()` | Deducts money if sufficient funds exist. |
| `transfer()` | Transfers money between accounts. |
| `transaction_history()` | Displays recorded transactions. |
| `change_pin()` | Updates the account PIN. |
| `close_account()` | Closes an eligible account. |
| `account_menu()` | Handles the logged-in user's menu. |

## 8. How Deposits and Withdrawals Work

### Deposit Example

Suppose the current balance is Rs. 5,000 and the user deposits Rs. 1,000.

The calculation is:

```text
New Balance = Current Balance + Deposit Amount

New Balance = 5000 + 1000

New Balance = Rs. 6000
```

In Python:

```python
accounts[account_number]["balance"] = round(
    accounts[account_number]["balance"] + amount, 2
)
```

The program then records the transaction and saves the updated dictionary.

### Withdrawal Example

Suppose the current balance is Rs. 5,000 and the user withdraws Rs. 2,000.

```text
New Balance = Current Balance - Withdrawal Amount

New Balance = 5000 - 2000

New Balance = Rs. 3000
```

Before deducting the amount, the application checks whether the requested withdrawal exceeds the available balance.

If it does, the operation is cancelled.

## 9. How Money Transfers Work

Suppose account `1001` has Rs. 5,000 and account `1002` has Rs. 3,000.

The user transfers Rs. 1,000 from account `1001` to account `1002`.

Before the transfer:

```text
Account 1001: Rs. 5000
Account 1002: Rs. 3000
Total:        Rs. 8000
```

After the transfer:

```text
Account 1001: Rs. 4000
Account 1002: Rs. 4000
Total:        Rs. 8000
```

The transfer function performs the following operations:

1. Checks whether the receiver exists.
2. Prevents transfers to the same account.
3. Validates the transfer amount.
4. Checks the sender's available balance.
5. Deducts the amount from the sender.
6. Adds the amount to the receiver.
7. Records the outgoing transaction for the sender.
8. Records the incoming transaction for the receiver.
9. Saves the updated account dictionary.

Recording the transaction for both accounts allows both users to see their respective sides of the transfer.

## 10. Transaction History

Each account contains a list called `transactions`.

For example:

```python
"transactions": [
    "27-10-2026 10:00:00 - Account created with Rs. 5000.0",
    "27-10-2026 10:10:00 - Deposited Rs. 1000.00",
    "27-10-2026 10:15:00 - Withdrew Rs. 500.00"
]
```

The `add_transaction()` function generates a timestamp using Python's `datetime` module.

```python
time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
account["transactions"].append(time + " - " + message)
```

The `datetime.now()` function obtains the current local date and time.

The `strftime()` method formats it into a readable string.

The `append()` method adds the new transaction to the list.

The transaction list is saved as part of the account data in the JSON file.

## 11. Input Validation

BankEase includes basic validation to prevent common invalid inputs.

| Input | Validation |
|---|---|
| Account number | Must contain digits and be unique. |
| Name | Must not be empty. |
| Age | Must be a positive integer. |
| Phone number | Must contain exactly ten digits. |
| Address | Must not be empty. |
| Account type | Must be Savings or Current. |
| PIN | Must contain exactly four digits. |
| Deposit | Must be a positive numeric amount. |
| Withdrawal | Must be positive and cannot exceed the balance. |
| Transfer | Receiver must exist, sender and receiver must differ, and sufficient funds must be available. |
| New PIN | Must be valid, different from the current PIN, and confirmed correctly. |

The application uses `while` loops to ask the user to retry when input is invalid.

The validation is basic rather than comprehensive. For example, it does not verify that a phone number belongs to the user or that an address is genuine.

## 12. Python Concepts Used

### Dictionaries

Dictionaries store account details as key-value pairs. BankEase uses a dictionary of dictionaries to organize multiple accounts.

### Lists

Lists store the transaction history for each account.

### Functions

Functions divide the application into smaller, reusable operations. This makes the code easier to understand, test, and maintain.

### Loops

`while` loops keep the menus running and repeat input prompts until valid values are entered.

A `for` loop is used for the three PIN attempts and for displaying transaction history.

### Conditional Statements

`if`, `elif`, and `else` statements implement decision-making, such as checking account existence, verifying PINs, and determining whether a withdrawal is allowed.

### File Handling

The `open()` function accesses the JSON file. The `with` statement manages the file's lifecycle.

### JSON Module

The built-in `json` module reads and writes structured account data.

### OS Module

The built-in `os` module checks whether the JSON file exists.

### Datetime Module

The built-in `datetime` module provides timestamps for transaction records.

### String Methods

The program uses methods such as `strip()`, `isdigit()`, `lower()`, `capitalize()`, and `replace()` for input processing and validation.

### Exception Handling

The `try` and `except` statements handle invalid JSON syntax during data loading.

### F-Strings

F-strings format account details and monetary values for readable output.

### The `__name__` Check

```python
if __name__ == "__main__":
    main()
```

This ensures that `main()` runs when the file is executed directly. It does not automatically run when the file is imported as a module.

## 13. Installation and Execution

### Requirements

- Python 3.8 or later is recommended.
- No third-party packages are required.
- A terminal or command prompt.

The project uses only Python's standard library.

### Steps

1. Create a folder named `BankEase`.
2. Save the complete program as `bankease.py`.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python bankease.py
```

On some systems, use:

```bash
python3 bankease.py
```

The program creates `accounts.json` automatically if it does not exist.

Create an account, log in, and test the available operations.

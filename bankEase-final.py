import json
import os
from datetime import datetime

ACCOUNTS_FILE = "accounts.json"


# ==================== JSON STORAGE ====================

def load_data():
    """Load account data from the JSON file."""

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


def save_data(accounts):
    """Save account data to the JSON file."""

    with open(ACCOUNTS_FILE, "w") as file:
        json.dump(accounts, file, indent=4)


# ==================== HELPER FUNCTIONS ====================

def account_exists(account_number, accounts):
    return account_number in accounts


def is_valid_pin(pin):
    return len(pin) == 4 and pin.isdigit()


def is_valid_phone(phone):
    return len(phone) == 10 and phone.isdigit()


def is_valid_amount(amount):
    if amount.isdigit():
        return float(amount) > 0

    if amount.count(".") == 1:
        return amount.replace(".", "", 1).isdigit() and float(amount) > 0

    return False


def get_amount(message):
    """Get a valid positive amount from the user."""

    while True:
        amount = input(message).strip()

        if is_valid_amount(amount):
            return round(float(amount), 2)

        print("Please enter a valid positive amount.")


def add_transaction(account, message):
    """Add a transaction with its date and time."""

    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    account["transactions"].append(time + " - " + message)


# ==================== CREATE ACCOUNT ====================

def create_account(accounts):

    print("\n========== CREATE ACCOUNT ==========")

    while True:
        account_number = input("Enter account number: ").strip()

        if not account_number.isdigit():
            print("Account number must contain only digits.")

        elif account_exists(account_number, accounts):
            print("Account number already exists.")

        else:
            break

    name = input("Enter full name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    while True:
        age = input("Enter age: ").strip()

        if age.isdigit() and int(age) > 0:
            age = int(age)
            break

        print("Please enter a valid age.")

    while True:
        phone = input("Enter phone number (10 digits): ").strip()

        if is_valid_phone(phone):
            break

        print("Phone number must contain exactly 10 digits.")

    address = input("Enter address: ").strip()

    if not address:
        print("Address cannot be empty.")
        return

    while True:
        account_type = input(
            "Enter account type (Savings/Current): "
        ).strip().lower()

        if account_type in ["savings", "current"]:
            account_type = account_type.capitalize()
            break

        print("Please enter Savings or Current.")

    while True:
        pin = input("Create a 4-digit PIN: ").strip()

        if is_valid_pin(pin):
            break

        print("PIN must contain exactly 4 digits.")

    deposit = get_amount("Enter initial deposit (Rs.): ")

    accounts[account_number] = {
        "name": name,
        "age": age,
        "phone": phone,
        "address": address,
        "type": account_type,
        "pin": pin,
        "balance": deposit,
        "transactions": []
    }

    add_transaction(
        accounts[account_number],
        "Account created with Rs. " + str(deposit)
    )

    save_data(accounts)

    print("\nAccount created successfully.")
    print("Account Number:", account_number)
    print("Account Holder:", name)
    print("Initial Balance: Rs.", format(deposit, ".2f"))


# ==================== LOGIN ====================

def login(accounts):

    print("\n========== ACCOUNT LOGIN ==========")

    account_number = input("Enter account number: ").strip()

    if not account_exists(account_number, accounts):
        print("Account not found.")
        return None

    for attempt in range(3):
        pin = input("Enter PIN: ").strip()

        if accounts[account_number]["pin"] == pin:
            print("Login successful.")
            print("Welcome,", accounts[account_number]["name"])
            return account_number

        print("Incorrect PIN. Attempts remaining:", 2 - attempt)

    print("Too many incorrect attempts. Please try again later.")
    return None


# ==================== ACCOUNT DETAILS ====================

def account_details(account_number, accounts):

    account = accounts[account_number]

    print("\n========== ACCOUNT DETAILS ==========")
    print("Account Number :", account_number)
    print("Name           :", account["name"])
    print("Age            :", account["age"])
    print("Phone          :", account["phone"])
    print("Address        :", account["address"])
    print("Account Type   :", account["type"])
    print("Balance        : Rs.", format(account["balance"], ".2f"))
    print("=====================================")


# ==================== CHECK BALANCE ====================

def check_balance(account_number, accounts):

    balance = accounts[account_number]["balance"]

    print("\nCurrent Balance: Rs.", format(balance, ".2f"))


# ==================== DEPOSIT MONEY ====================

def deposit(account_number, accounts):

    print("\n========== DEPOSIT MONEY ==========")

    amount = get_amount("Enter deposit amount (Rs.): ")

    accounts[account_number]["balance"] = round(
        accounts[account_number]["balance"] + amount, 2
    )

    add_transaction(
        accounts[account_number],
        "Deposited Rs. " + format(amount, ".2f")
    )

    save_data(accounts)

    print("Deposit successful.")
    print("Deposited Amount: Rs.", format(amount, ".2f"))
    print(
        "New Balance: Rs.",
        format(accounts[account_number]["balance"], ".2f")
    )


# ==================== WITHDRAW MONEY ====================

def withdraw(account_number, accounts):

    print("\n========== WITHDRAW MONEY ==========")

    amount = get_amount("Enter withdrawal amount (Rs.): ")

    balance = accounts[account_number]["balance"]

    if amount > balance:
        print("Insufficient balance.")
        print("Available Balance: Rs.", format(balance, ".2f"))
        return

    accounts[account_number]["balance"] = round(balance - amount, 2)

    add_transaction(
        accounts[account_number],
        "Withdrew Rs. " + format(amount, ".2f")
    )

    save_data(accounts)

    print("Withdrawal successful.")
    print("Withdrawn Amount: Rs.", format(amount, ".2f"))
    print(
        "Remaining Balance: Rs.",
        format(accounts[account_number]["balance"], ".2f")
    )


# ==================== TRANSFER MONEY ====================

def transfer(account_number, accounts):

    print("\n========== TRANSFER MONEY ==========")

    receiver_number = input("Enter receiver account number: ").strip()

    if not account_exists(receiver_number, accounts):
        print("Receiver account not found.")
        return

    if receiver_number == account_number:
        print("You cannot transfer money to your own account.")
        return

    amount = get_amount("Enter transfer amount (Rs.): ")

    sender_balance = accounts[account_number]["balance"]

    if amount > sender_balance:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] = round(
        sender_balance - amount, 2
    )

    accounts[receiver_number]["balance"] = round(
        accounts[receiver_number]["balance"] + amount, 2
    )

    add_transaction(
        accounts[account_number],
        "Transferred Rs. " + format(amount, ".2f")
        + " to account " + receiver_number
    )

    add_transaction(
        accounts[receiver_number],
        "Received Rs. " + format(amount, ".2f")
        + " from account " + account_number
    )

    save_data(accounts)

    print("Transfer successful.")
    print("Amount Transferred: Rs.", format(amount, ".2f"))
    print("Receiver Account:", receiver_number)
    print(
        "Remaining Balance: Rs.",
        format(accounts[account_number]["balance"], ".2f")
    )


# ==================== TRANSACTION HISTORY ====================

def transaction_history(account_number, accounts):

    print("\n========== TRANSACTION HISTORY ==========")

    transactions = accounts[account_number]["transactions"]

    if not transactions:
        print("No transactions found.")
        return

    for number, transaction in enumerate(transactions, start=1):
        print(str(number) + ".", transaction)


# ==================== CHANGE PIN ====================

def change_pin(account_number, accounts):

    print("\n========== CHANGE PIN ==========")

    current_pin = input("Enter current PIN: ").strip()

    if current_pin != accounts[account_number]["pin"]:
        print("Incorrect current PIN.")
        return

    while True:
        new_pin = input("Enter new 4-digit PIN: ").strip()

        if not is_valid_pin(new_pin):
            print("PIN must contain exactly 4 digits.")
            continue

        if new_pin == current_pin:
            print("New PIN must be different from the current PIN.")
            continue

        confirm_pin = input("Confirm new PIN: ").strip()

        if new_pin != confirm_pin:
            print("PINs do not match. Try again.")
            continue

        break

    accounts[account_number]["pin"] = new_pin

    add_transaction(
        accounts[account_number],
        "Account PIN changed"
    )

    save_data(accounts)

    print("PIN changed successfully.")


# ==================== CLOSE ACCOUNT ====================

def close_account(account_number, accounts):

    print("\n========== CLOSE ACCOUNT ==========")

    balance = accounts[account_number]["balance"]

    if balance != 0:
        print("Account cannot be closed while the balance is not zero.")
        print("Current Balance: Rs.", format(balance, ".2f"))
        print("Withdraw or transfer the remaining balance first.")
        return False

    confirmation = input(
        "Are you sure you want to close this account? (Y/N): "
    ).strip().lower()

    if confirmation != "y":
        print("Account closure cancelled.")
        return False

    pin = input("Enter your PIN to confirm account closure: ").strip()

    if pin != accounts[account_number]["pin"]:
        print("Incorrect PIN. Account was not closed.")
        return False

    del accounts[account_number]

    save_data(accounts)

    print("Account closed successfully.")

    return True


# ==================== ACCOUNT MENU ====================

def account_menu(account_number, accounts):

    while True:

        print("\n====================================")
        print("          BANKEASE MENU")
        print("====================================")
        print("1. Account Details")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Transaction History")
        print("7. Change PIN")
        print("8. Close Account")
        print("9. Logout")
        print("====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            account_details(account_number, accounts)

        elif choice == "2":
            check_balance(account_number, accounts)

        elif choice == "3":
            deposit(account_number, accounts)

        elif choice == "4":
            withdraw(account_number, accounts)

        elif choice == "5":
            transfer(account_number, accounts)

        elif choice == "6":
            transaction_history(account_number, accounts)

        elif choice == "7":
            change_pin(account_number, accounts)

        elif choice == "8":
            if close_account(account_number, accounts):
                break

        elif choice == "9":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


# ==================== MAIN PROGRAM ====================

def main():

    accounts = load_data()

    while True:

        print("\n====================================")
        print("        WELCOME TO BANKEASE")
        print("====================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            account_number = login(accounts)

            if account_number is not None:
                account_menu(account_number, accounts)

        elif choice == "3":
            print("Thank you for using BankEase.")
            break

        else:
            print("Invalid choice. Please try again.")


# ==================== START PROGRAM ====================

if __name__ == "__main__":
    main()
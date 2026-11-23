import sqlite3
from pathlib import Path
from accounts import Account


class AccountModel:

    def __init__(self, database_path=Path(__file__).resolve().with_name("PyBank.db")):
        self.database_path = database_path
        self.current_username = None
        self.current_account = None

    def validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

    def authenticate_user(self, username, password):
        connection = sqlite3.connect(self.database_path)
        try:
            row = connection.execute(
                """
                SELECT AccountBalance
                FROM User
                WHERE Username = ? AND Password = ?
                """,
                (username, password),
            ).fetchone()
        finally:
            connection.close()

        if row is None:
            self.current_username = None
            self.current_account = None
            return False

        self.current_username = username
        self.current_account = Account(username, row[0])
        return True

    def get_balance(self, username):
        connection = sqlite3.connect(self.database_path)
        try:
            row = connection.execute(
                "SELECT AccountBalance FROM User WHERE Username = ?",
                (username,),
            ).fetchone()
        finally:
            connection.close()

        if row is None:
            raise LookupError("Account was not found.")

        balance = row[0]
        if username == self.current_username:
            self.current_account = Account(username, balance)
        return balance

    def deposit(self, username, amount):
        self.validate_amount(amount)
        connection = sqlite3.connect(self.database_path)
        try:
            cursor = connection.execute(
                """
                UPDATE User
                SET AccountBalance = AccountBalance + ?
                WHERE Username = ?
                """,
                (amount, username),
            )
            if cursor.rowcount == 0:
                raise LookupError("Account was not found.")
            connection.commit()
        finally:
            connection.close()

        self.get_balance(username)
        return True

    def withdraw(self, username, amount):
        self.validate_amount(amount)
        connection = sqlite3.connect(self.database_path)
        try:
            cursor = connection.execute(
                """
                UPDATE User
                SET AccountBalance = AccountBalance - ?
                WHERE Username = ? AND AccountBalance >= ?
                """,
                (amount, username, amount),
            )
            if cursor.rowcount == 0:
                exists = connection.execute(
                    "SELECT 1 FROM User WHERE Username = ?",
                    (username,),
                ).fetchone()
                if exists is None:
                    raise LookupError("Account was not found.")
                return False
            connection.commit()
        finally:
            connection.close()

        self.get_balance(username)
        return True

    def update_balance(self, username, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")

        connection = sqlite3.connect(self.database_path)
        try:
            cursor = connection.execute(
                "UPDATE User SET AccountBalance = ? WHERE Username = ?",
                (new_balance, username),
            )
            if cursor.rowcount == 0:
                raise LookupError("Account was not found.")
            connection.commit()
        finally:
            connection.close()

        self.get_balance(username)

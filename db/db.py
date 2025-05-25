import sqlite3
import json


def init_db(data) -> None:
    """Réinitialisation de la base de données

    Args:
        data (dict): dictionnaire contenant les données du fichier JSON

    """
    with sqlite3.connect("budget.db") as conn:

        cur = conn.cursor()

        # deleting table "users"
        print("Deleting the table: users")
        cur.execute(
            """
            DROP TABLE IF EXISTS users
        """
        )

        # creating table "users"
        print("Creating the table: users")
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """
        )

        # deleting table "accounts"
        print("Deleting the table: accounts")
        cur.execute(
            """
            DROP TABLE IF EXISTS accounts
        """
        )

        # creating table "accounts"
        print("Creating the table: accounts")
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                balance REAL NOT NULL,
                date_balance TEXT NOT NULL,
                type TEXT NOT NULL,
                in_budget INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """
        )

        # deleting table "payees"
        print("Deleting the table: payees")
        cur.execute(
            """
            DROP TABLE IF EXISTS payees
        """
        )

        # creating table "payees"
        print("Creating the table: payees")
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS payees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """
        )

        # deleting table "transactions"
        print("Deleting the table: transactions")
        cur.execute(
            """
            DROP TABLE IF EXISTS transactions
        """
        )

        # creating table "transactions"
        print("Creating the table: transactions")
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_transaction TEXT NOT NULL,
                payee_id INTEGER NOT NULL,
                sub_category_id INTEGER NOT NULL,
                memo TEXT NOT NULL,
                outflow REAL,
                inflow REAL,
                committed INTEGER NOT NULL,
                account_id INTEGER NOT NULL,
                FOREIGN KEY (payee_id) REFERENCES payees(id),
                FOREIGN KEY (account_id) REFERENCES accounts(id)
            )
        """
        )

        # deleting table "scheduled_transactions"
        print("Deleting the table: scheduled_transactions")
        cur.execute(
            """
            DROP TABLE IF EXISTS scheduled_transactions
        """
        )

        # creating table "scheduled_transactions"
        print("Creating the table: scheduled_transactions")
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS scheduled_transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_transaction TEXT NOT NULL,
                payee_id INTEGER NOT NULL,
                sub_category_id INTEGER NOT NULL,
                memo TEXT NOT NULL,
                outflow REAL,
                inflow REAL,
                frequency TEXT NOT NULL,
                account_id INTEGER NOT NULL,
                FOREIGN KEY (payee_id) REFERENCES payees(id),
                FOREIGN KEY (account_id) REFERENCES accounts(id)
            )
        """
        )

        # deleting table "top_categories"
        print("Deleting the table: top_categories")
        cur.execute(
            """
            DROP TABLE IF EXISTS top_categories
        """
        )

        # creating table "top_categories"
        print("Creating the table: top_categories")
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS top_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """
        )

        # deleting table "sub_categories"
        print("Deleting the table: sub_categories")
        cur.execute(
            """
            DROP TABLE IF EXISTS sub_categories
        """
        )

        # creating table "sub_categories"
        print("Creating the table: sub_categories")
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS sub_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                top_category_id INTEGER NOT NULL,
                FOREIGN KEY (top_category_id) REFERENCES top_categories(id)
            )
        """
        )

        print(f"Populating table users")
        users = data.get("users")

        cur.executemany(
            """
            INSERT INTO users (email, firstname, lastname, password)
                VALUES (:email, :firstname, :lastname, :password)
            """,
            users,
        )

        print(f"Populating table accounts")
        accounts = data.get("accounts")

        cur.executemany(
            """
            INSERT INTO accounts (name, balance, date_balance, type, in_budget, user_id)
                VALUES (:name, :balance, :date_balance, :type, :in_budget, :user_id)
            """,
            accounts,
        )

        print(f"Populating table top_categories")
        top_categories = data.get("top_categories")

        cur.executemany(
            """
            INSERT INTO top_categories (name)
                VALUES (:name)
            """,
            top_categories,
        )

        print(f"Populating table sub_categories")
        sub_categories = data.get("sub_categories")

        cur.executemany(
            """
            INSERT INTO sub_categories (name, top_category_id)
                VALUES (:name, :top_category_id)
            """,
            sub_categories,
        )

        print(f"Populating table payees")
        payees = data.get("payees")

        cur.executemany(
            """
            INSERT INTO payees (name)
                VALUES (:name)
            """,
            payees,
        )

        print(f"Populating table transactions")
        transactions = data.get("transactions")

        cur.executemany(
            """
            INSERT INTO transactions (date_transaction, payee_id, sub_category_id, memo, outflow, inflow, committed, account_id)
                VALUES (:date_transaction, :payee_id, :sub_category_id, :memo, :outflow, :inflow, :committed, :account_id)
            """,
            transactions,
        )

        print(f"Populating table scheduled_transactions")
        scheduled_transactions = data.get("scheduled_transactions")

        cur.executemany(
            """
            INSERT INTO scheduled_transactions (date_transaction, payee_id, sub_category_id, memo, outflow, inflow, frequency, account_id)
                VALUES (:date_transaction, :payee_id, :sub_category_id, :memo, :outflow, :inflow, :frequency, :account_id)
            """,
            scheduled_transactions,
        )


def read_json(fichier: str) -> dict:
    """Lecture du fichier JSON contenant les données

    Args:
        fichier (str): URI vers le fichier JSON contenant les données

    Returns:
        dict: contenu du fichier de données sous forme de dictionnaire
    """
    data = {}
    with open(fichier, "r", encoding="utf-8") as fic:
        data = json.load(fic)

    return data


entree = input(
    "Attention! Ce script va reinitialiser la base de donnees. Continuer (O/N)"
)
if entree.upper() == "O":
    data = read_json("db/data.json")
    init_db(data)


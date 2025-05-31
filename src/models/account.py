class Account:

    def __init__(self, id: int, name: str, balance: float, date_balance: str, type_account: str, in_budget: int, user_id: int) -> None:
        self.id = id
        self.name = name
        self.balance = balance
        self.date_balance = date_balance
        self.type_account = type_account
        self.in_budget = in_budget
        self.user_id = user_id

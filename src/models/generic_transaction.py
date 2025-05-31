class GenericTransaction:

    def __init__(self, id: int, date_transaction: str, payee_id: int, sub_category: int, memo: str, outflow: float, inflow: float, account_id: int) -> None:
        self.id = id
        self.date_transaction = date_transaction
        self.payee_id = payee_id
        self.sub_category = sub_category
        self.memo = memo
        self.outflow = outflow
        self.inflow = inflow
        self.account_id = account_id

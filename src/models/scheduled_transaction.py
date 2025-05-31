from src.models.generic_transaction import GenericTransaction

class ScheduledTransaction(GenericTransaction) :

    def __init__(self, id: int, date_transaction: str, payee_id: int, sub_category: int, memo: str, outflow: float, inflow: float, account_id: int, frequency: str) -> None:
        super().__init__(id, date_transaction, payee_id, sub_category, memo, outflow, inflow, account_id)
        self.frequency = frequency

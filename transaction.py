from abc import abstractmethod
import uuid
from datetime import datetime

class Transaction:
    def __init__(self, accountId, amount: float, note: str, date: datetime) -> None:
        self.id = uuid.uuid4()
        self.accountId = accountId
        self.amount = amount
        self.note = note
        self.date = datetime.now()

    def __str__(self) -> str:
        return f"{self.amount} {self.note} {self.date}"
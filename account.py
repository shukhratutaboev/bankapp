import uuid

class Account:
    def __init__(self, cardNumber, name: str) -> None:
        self.id = uuid.uuid4()
        self.numberId = cardNumber
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

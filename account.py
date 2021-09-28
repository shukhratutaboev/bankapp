import uuid
import random

class Account:
    def __init__(self, name: str) -> None:
        self.id = uuid.uuid4()
        self.numberId = random.randint(8600000000000001,8600999999999999)
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

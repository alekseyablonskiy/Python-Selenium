from dataclasses import dataclass


@dataclass
class Card:
    name: str = "testName"
    card_num: str = "12344321"
    cvc: str = "123"
    month: str = "12"
    year: str = "2025"


from dataclasses import dataclass


@dataclass
class ReviewData:
    name: str = 'TestName'
    email: str = 'test@mail.ru'
    review: str = 'some test text'
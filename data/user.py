from dataclasses import dataclass


@dataclass
class User:
    name: str = "testName"
    email: str = "testEmail12@q.com"
    password: str = "123"
    first_name: str = "Ivan"
    last_name: str = "Budko"
    address: str = "Loogle"
    country: str = "Australia"
    state: str = "Gachinsk"
    city: str = "Muchinsk"
    zipcode: str = "232323"
    mobile_number: str = "37511111"



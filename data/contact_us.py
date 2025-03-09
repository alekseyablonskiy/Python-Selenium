from dataclasses import dataclass


@dataclass
class ContactUs:
    name: str = "testName"
    email: str = "testEmail11@q.com"
    subject: str = "testSubject"
    message: str = "some text"
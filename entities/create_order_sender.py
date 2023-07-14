from xml.etree import ElementTree as ET


class CreateOrderSender:
    def __init__(
        self,
        company: str,
        person: str,
        phone: str,
        town: str,
        address: str,
        date: str,
        timeMin: str,
        timeMax: str,
    ):
        self.company = company
        self.person = person
        self.phone = phone
        self.town = town
        self.address = address
        self.date = date
        self.timeMin = timeMin
        self.timeMax = timeMax
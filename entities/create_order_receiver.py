from xml.etree import ElementTree as ET


class CreateOrderReceiver:
    def __init__(
        self,
        company: str,
        person: str,
        phone: str,
        zipcode: str,
        town: str,
        regionCode: str,
        address: str,
        date: str,
        timeMin: str,
        timeMax: str,
        pvzCode: str,
    ):
        self.company = company
        self.person = person
        self.phone = phone
        self.zipcode = zipcode
        self.town = town
        self.regionCode = regionCode
        self.address = address
        self.date = date
        self.timeMin = timeMin
        self.timeMax = timeMax
        self.pvzCode = pvzCode
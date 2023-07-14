from typing import List, Dict
import xml.etree.ElementTree as ET

from entities.abstract_object import AbstractObject
from entities.town import Town


class Sender(AbstractObject):
    def __init__(
        self,
        company: str,
        person: str,
        phone: str,
        contacts: List[Dict[str, str]],
        town: Town,
        address: str,
        date: str,
        timeMin: str,
        timeMax: str,
    ):
        self.company = company
        self.person = person
        self.phone = phone
        self.contacts = contacts
        self.town = town
        self.address = address
        self.date = date
        self.timeMin = timeMin
        self.timeMax = timeMax

    @staticmethod
    def get_from_xml(xml: ET.Element, from_node: bool = True) -> "Sender":
        contacts = []
        if xml.find("contacts") is not None:
            for contact in xml.find("contacts").getchildren():
                contacts.append(
                    {
                        "name": contact.tag,
                        "value": Sender.extract_xml_value(contact, "", False),
                    }
                )

        params = {
            "company": Sender.extract_xml_value(xml, "company", from_node),
            "person": Sender.extract_xml_value(xml, "person", from_node),
            "phone": Sender.extract_xml_value(xml, "phone", from_node),
            "address": Sender.extract_xml_value(xml, "address", from_node),
            "date": Sender.extract_xml_value(xml, "date", from_node),
            "timeMin": Sender.extract_xml_value(xml, "time_min", from_node),
            "timeMax": Sender.extract_xml_value(xml, "time_max", from_node),
            "contacts": contacts,
            "town": Town.get_from_xml(xml.find("town"), False)
            if xml.find("town") is not None
            else None,
        }

        return Sender(**params)

    def get_company(self) -> str:
        return self.company

    def get_person(self) -> str:
        return self.person

    def get_phone(self) -> str:
        return self.phone

    def get_contacts(self) -> List[Dict[str, str]]:
        return self.contacts

    def get_town(self) -> Town:
        return self.town

    def get_address(self) -> str:
        return self.address

    def get_date(self) -> str:
        return self.date

    def get_time_min(self) -> str:
        return self.timeMin

    def get_time_max(self) -> str:
        return self.timeMax

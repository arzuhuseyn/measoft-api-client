from xml.etree import ElementTree as ET

from entities.abstract_object import AbstractObject
from entities.pvz import Pvz
from entities.town import Town


class Receiver(AbstractObject):
    """Получатель"""

    def __init__(
        self,
        company: str = None,
        person: str = None,
        phone: str = None,
        contacts: list = None,
        zipcode: str = None,
        town: Town = None,
        address: str = None,
        date: str = None,
        time_min: str = None,
        time_max: str = None,
        coordinates: dict = None,
        pvz: Pvz = None,
    ):
        self.company = company
        self.person = person
        self.phone = phone
        self.contacts = contacts or []
        self.zipcode = zipcode
        self.town = town
        self.address = address
        self.date = date
        self.time_min = time_min
        self.time_max = time_max
        self.coordinates = coordinates or {}
        self.pvz = pvz

    @staticmethod
    def get_from_xml(xml: ET.Element, from_node: bool = True):
        contacts = []
        coordinates = {}

        if xml.find("contacts") is not None:
            for contact in xml.find("contacts").getchildren():
                contacts.append(
                    {
                        "name": contact.tag,
                        "value": contact.text,
                    }
                )

        if xml.find("town") is not None:
            town = Town.get_from_xml(xml.find("town"), False)
        else:
            town = None

        if xml.find("pvz") is not None:
            pvz = Pvz.get_from_xml(xml.find("pvz"))
        else:
            pvz = None

        if xml.find("coords") is not None:
            coordinates = {
                "latitude": float(xml.find("coords").find("lat").text),
                "longitude": float(xml.find("coords").find("lon").text),
            }

        return Receiver(
            company=Receiver.extract_xml_value(xml, "company", from_node),
            person=Receiver.extract_xml_value(xml, "person", from_node),
            phone=Receiver.extract_xml_value(xml, "phone", from_node),
            zipcode=Receiver.extract_xml_value(xml, "zipcode", from_node),
            address=Receiver.extract_xml_value(xml, "address", from_node),
            date=Receiver.extract_xml_value(xml, "date", from_node),
            time_min=Receiver.extract_xml_value(xml, "time_min", from_node),
            time_max=Receiver.extract_xml_value(xml, "time_max", from_node),
            contacts=contacts,
            coordinates=coordinates,
            town=town,
            pvz=pvz,
        )

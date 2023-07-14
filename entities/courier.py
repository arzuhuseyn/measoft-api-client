from xml.etree import ElementTree as ET

from entities.abstract_object import AbstractObject


class Courier(AbstractObject):
    def __init__(self, code: str, name: str, phone: str):
        self.code = code
        self.name = name
        self.phone = phone

    @staticmethod
    def get_from_xml(xml: ET.Element, from_node: bool = True) -> "Courier":
        params = {
            "code": Courier.extract_xml_value(xml, "code", from_node),
            "name": Courier.extract_xml_value(xml, "name", from_node),
            "phone": Courier.extract_xml_value(xml, "phone", from_node),
        }

        return Courier(**params)

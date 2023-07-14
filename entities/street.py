from xml.etree import ElementTree as ET

from entities.abstract_object import AbstractObject


class Street(AbstractObject):
    def __init__(self, name: str, shortName: str, typeName: str):
        self.name = name
        self.shortName = shortName
        self.typeName = typeName

    @staticmethod
    def get_from_xml(self, xml: ET.Element, from_node: bool = True) -> 'Street':
        params = {
            'name': Street.extract_xml_value(xml, 'name', from_node),
            'shortName': self.extract_xml_value(xml, 'shortname', from_node),
            'typeName': self.extract_xml_value(xml, 'typename', from_node),
        }

        return Street(**params)

    def get_name(self) -> str:
        return self.name

    def get_short_name(self) -> str:
        return self.shortName

    def get_type_name(self) -> str:
        return self.typeName
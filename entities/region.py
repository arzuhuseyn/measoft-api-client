from xml.etree import ElementTree as ET

from entities.abstract_object import AbstractObject
from entities.country import Country


class Region(AbstractObject):
    def __init__(self, code: str, name: str, country: Country):
        self.code = code
        self.name = name
        self.country = country

    @staticmethod
    def get_from_xml(xml: ET.Element, from_node: bool = True) -> 'Region':
        if from_node:
            code = xml.findtext('code')
            name = xml.findtext('name')
            country = Country.get_from_xml(xml.find('country'))
        else:
            code = xml.attrib['code']
            name = xml.text
            country = None

        return Region(code, name, country)

    def get_code(self) -> str:
        return self.code

    def set_code(self, code: str) -> 'Region':
        self.code = code
        return self

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> 'Region':
        self.name = name
        return self

    def get_country(self) -> Country:
        return self.country
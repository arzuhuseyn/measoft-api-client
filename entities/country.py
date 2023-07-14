import xml.etree.ElementTree as ET

from entities.abstract_object import AbstractObject


class Country(AbstractObject):
    def __init__(self, id: str, code: str, name: str, shortName1: str, shortName2: str):
        self.id = id
        self.code = code
        self.name = name
        self.shortName1 = shortName1
        self.shortName2 = shortName2

    @staticmethod
    def get_from_xml(xml: ET.Element, from_node: bool = True) -> 'Country':
        params = {
            'id': xml.findtext('id') if from_node else xml.text,
            'code': xml.findtext('code') if from_node else xml.text,
            'name': xml.findtext('name') if from_node else xml.text,
            'shortName1': xml.findtext('ShortName1') if from_node else xml.text,
            'shortName2': xml.findtext('ShortName2') if from_node else xml.text,
        }

        return Country(**params)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Country {self.code}: {self.name}>'

    def __eq__(self, other):
        if isinstance(other, Country):
            return self.code == other.code
        elif isinstance(other, str):
            return self.code == other
        else:
            return False

    def __hash__(self):
        return hash(self.code)

    def get_id(self) -> str:
        return self.id

    def get_code(self) -> str:
        return self.code

    def get_name(self) -> str:
        return self.name

    def get_short_name1(self) -> str:
        return self.shortName1

    def get_short_name2(self) -> str:
        return self.shortName2
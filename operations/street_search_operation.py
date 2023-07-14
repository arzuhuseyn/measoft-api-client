from typing import List
from xml.etree.ElementTree import Element

from operations import AbstractOperation
from api import MeasoftApi as Api
from entities import Street



class StreetSearchOperation(AbstractOperation):
    def __init__(self, api: Api):
        super().__init__(api)
        self.town = None
        self.name_contains = None
        self.name_starts = None
        self.name = None
        self.full_name = None

    def town(self, town: str):
        self.town = town
        return self

    def name_contains(self, name_contains: str):
        self.name_contains = name_contains
        return self

    def name_starts(self, name_starts: str):
        self.name_starts = name_starts
        return self

    def name(self, name: str):
        self.name = name
        return self

    def full_name(self, full_name: str):
        self.full_name = full_name
        return self

    def build_xml(self) -> Element:
        xml = self.create_xml('streetlist')
        conditions = xml.add_child('conditions')

        conditions.add_child('town', self.town)
        conditions.add_child('namecontains', self.name_contains)
        conditions.add_child('namestarts', self.name_starts)
        conditions.add_child('name', self.name)
        conditions.add_child('fullname', self.full_name)

        self.build_limit_xml(xml)

        return xml

    def search(self) -> List[Street]:
        if not self.town:
            raise Exception('Не указан населенный пункт')

        result = []
        for item in self.get_results(False):
            result.append(Street.get_from_xml(item))

        return result
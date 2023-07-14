from typing import List
from xml.etree.ElementTree import Element as SimpleXMLElement

from operations import AbstractOperation
from api import MeasoftApi as Api
from entities import Pvz


class PvzSearchOperation(AbstractOperation):
    def __init__(self, api: Api):
        super().__init__(api)
        self.town = None
        self.code = None
        self.parent_code = None
        self.accept_cash = None
        self.accept_card = None
        self.accept_fitting = None
        self.accept_individuals = None
        self.coordinates = None

    def town(self, town: str):
        self.town = town
        return self

    def code(self, code: int):
        self.code = code
        return self

    def parent_code(self, parent_code: str):
        self.parent_code = parent_code
        return self

    def accept_cash(self, accept_cash: bool):
        self.accept_cash = 'YES' if accept_cash else 'NO'
        return self

    def accept_card(self, accept_card: bool):
        self.accept_card = 'YES' if accept_card else 'NO'
        return self

    def accept_fitting(self, accept_fitting: bool):
        self.accept_fitting = 'YES' if accept_fitting else 'NO'
        return self

    def accept_individuals(self, accept_individuals: bool):
        self.accept_individuals = 'YES' if accept_individuals else 'NO'
        return self

    def coordinates(self, lt: float = None, lg: float = None, rt: float = None, rg: float = None):
        self.coordinates = {
            'lt': lt,
            'lg': lg,
            'rt': rt,
            'rg': rg,
        }
        return self

    def build_xml(self) -> SimpleXMLElement:
        xml = self.create_xml('pvzlist')
        self.build_limit_xml(xml)

        xml.add_child('town', self.town)
        xml.add_child('code', self.code)
        xml.add_child('parentcode', self.parent_code)
        xml.add_child('acceptcash', self.accept_cash)
        xml.add_child('acceptcard', self.accept_card)
        xml.add_child('acceptfitting', self.accept_fitting)
        xml.add_child('acceptindividuals', self.accept_individuals)
        xml.add_child('lt', self.coordinates['lt'] if self.coordinates else None)
        xml.add_child('lg', self.coordinates['lg'] if self.coordinates else None)
        xml.add_child('rt', self.coordinates['rt'] if self.coordinates else None)
        xml.add_child('rg', self.coordinates['rg'] if self.coordinates else None)

        return xml

    def search(self) -> List[Pvz]:
        return [Pvz.get_from_xml(item) for item in self.get_results()]
from typing import List
from xml.etree.ElementTree import Element as SimpleXMLElement

from operations.abstract_operation import AbstractOperation
from api import MeasoftApi as Api
from entities import CalculationResult


class CalculatorOperation(AbstractOperation):
    def __init__(self, api: Api):
        super().__init__(api)
        self.town_from = None
        self.town_to = None
        self.length = None
        self.width = None
        self.height = None
        self.weight = None
        self.service = None
    
    def set_town_from(self, town_from: str):
        self.town_from = town_from
        return self

    def set_town_to(self, town_to: str):
        self.town_to = town_to
        return self

    def set_length(self, length: float):
        self.length = length
        return self

    def set_width(self, width: float):
        self.width = width
        return self

    def set_height(self, height: float):
        self.height = height
        return self

    def set_weight(self, weight: float):
        self.weight = weight
        return self

    def set_service(self, service: int):
        self.service = service
        return self

    def build_xml(self) -> SimpleXMLElement:
        xml = self.create_xml('calculator')
        calc = xml.add_child('calc')

        calc.add_attribute('townfrom', self.town_from)
        calc.add_attribute('townto', self.town_to)
        calc.add_attribute('l', self.length)
        calc.add_attribute('w', self.width)
        calc.add_attribute('h', self.height)
        calc.add_attribute('mass', self.weight)
        calc.add_attribute('service', self.service)

        return xml

    def calculate(self) -> List[CalculationResult]:
        result = []
        for item in self.get_results():
            result.append(CalculationResult.get_from_xml(item))
        return result
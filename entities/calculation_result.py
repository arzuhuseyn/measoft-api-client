from xml.etree.ElementTree import Element as SimpleXMLElement

from entities.abstract_object import AbstractObject
from entities.town import Town


class CalculationResult(AbstractObject):
    def __init__(
        self,
        town_from: Town,
        town_to: Town,
        weight: float,
        service: int,
        service_name: str,
        zone: int,
        price: float,
        min_delivery_days: int,
        max_delivery_days: int,
    ):
        self.town_from = town_from
        self.town_to = town_to
        self.weight = weight
        self.service = service
        self.service_name = service_name
        self.zone = zone
        self.price = price
        self.min_delivery_days = min_delivery_days
        self.max_delivery_days = max_delivery_days

    @staticmethod
    def get_from_xml(
        xml: SimpleXMLElement, from_node: bool = True
    ) -> 'CalculationResult':
        town_from = (
            Town.get_from_xml(xml.townfrom, False) if hasattr(xml, "townfrom") else None
        )
        town_to = (
            Town.get_from_xml(xml.townto, False) if hasattr(xml, "townto") else None
        )

        return CalculationResult(
            town_from,
            town_to,
            float(xml.mass) if from_node else float(xml["mass"]),
            int(xml.service) if from_node else int(xml["service"]),
            xml.service.name if hasattr(xml.service, "name") else None,
            int(xml.zone) if from_node else int(xml["zone"]),
            float(xml.price) if from_node else float(xml["price"]),
            int(xml.mindeliverydays) if from_node else int(xml["mindeliverydays"]),
            int(xml.maxdeliverydays) if from_node else int(xml["maxdeliverydays"]),
        )

    def town_from(self, town_from: Town = None) -> Town:
        self.town_from = town_from
        return self

    def town_to(self, town_to: Town = None) -> Town:
        self.town_to = town_to
        return self

    def weight(self, weight: float = None) -> float:
        self.weight = weight
        return self

    def service(self, service: int = None) -> int:
        self.service = service
        return self

    def service_name(self, service_name: str = None) -> str:
        self.service_name = service_name
        return self

    def zone(self, zone: int = None) -> int:
        self.zone = zone
        return self

    def price(self, price: float = None) -> float:
        self.price = price
        return self

    def min_delivery_days(self, min_delivery_days: int = None) -> int:
        self.min_delivery_days = min_delivery_days
        return self

    def max_delivery_days(self, max_delivery_days: int = None) -> int:
        self.max_delivery_days = max_delivery_days
        return self

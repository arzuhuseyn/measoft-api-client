from typing import List
from xml.etree import ElementTree as ET

from api import MeasoftApi as Api

from operations import AbstractOperation


class CancelOrderOperation(AbstractOperation):
    def __init__(self, api: Api):
        super().__init__(api)
        self.order_code = None
        self.order_number = None

    def order_code(self, order_code: str) -> "CancelOrderOperation":
        self.order_code = order_code
        return self

    def order_number(self, order_number: str) -> "CancelOrderOperation":
        self.order_number = order_number
        return self

    def build_xml(self) -> ET.Element:
        xml = self.create_xml("cancelorder")
        order = ET.SubElement(xml, "order")
        order.set("orderno", self.order_number)
        order.set("ordercode", self.order_code)
        return xml

    def cancel(self):
        for item in self.get_results():
            error_code = int(item.get("error", 0))

            if error_code:
                raise Exception(
                    item.get(
                        "errormsgru", item.get("errormsg", "Код ошибки: " + error_code)
                    )
                )

            return

        raise Exception("Неизвестная ошибка")

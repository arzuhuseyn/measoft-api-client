from typing import List
from xml.etree.ElementTree import Element as SimpleXMLElement


from operations import AbstractOperation
from api import MeasoftApi as Api
from entities import Order


class OrderSearchOperation(AbstractOperation):
    def __init__(self, api: Api):
        super().__init__(api)
        self.orderNumber = None
        self.orderNumber2 = None
        self.orderCode = None
        self.givenCode = None
        self.dateFrom = None
        self.dateTo = None
        self.target = None
        self.done = None
        self.onlyLast = None
        self.quickStatus = None

    def order_number(self, order_number: str):
        self.orderNumber = order_number
        return self

    def order_number2(self, order_number2: str):
        self.orderNumber2 = order_number2
        return self

    def order_code(self, order_code: str):
        self.orderCode = order_code
        return self

    def given_code(self, given_code: str):
        self.givenCode = given_code
        return self

    def date_from(self, date_from: str):
        self.dateFrom = date_from
        return self

    def date_to(self, date_to: str):
        self.dateTo = date_to
        return self

    def target(self, target: str):
        self.target = target
        return self

    def done(self, done: int):
        self.done = {
            1: 'ONLY_NOT_DONE',
            2: 'ONLY_DONE',
            3: 'ONLY_NEW',
            4: 'ONLY_DELIVERY',
        }.get(done, None)
        return self

    def only_last(self, only_last: bool = True):
        self.onlyLast = 'ONLY_LAST' if only_last else None
        return self

    def set_quick_status(self, quick_status: bool = True):
        self.quickStatus = 'YES' if quick_status else 'NO'
        return self

    def build_xml(self) -> SimpleXMLElement:
        xml = self.create_xml('statusreq')
        self.build_client_xml(xml)
        xml.add_child('orderno', self.orderNumber)
        xml.add_child('orderno2', self.orderNumber2)
        xml.add_child('ordercode', self.orderCode)
        xml.add_child('givencode', self.givenCode)
        xml.add_child('datefrom', self.dateFrom)
        xml.add_child('dateto', self.dateTo)
        xml.add_child('target', self.target)
        xml.add_child('done', self.done)
        xml.add_child('changes', self.onlyLast)
        xml.add_child('quickstatus', self.quickStatus)
        self.build_stream_id_xml(xml)
        return xml

    def search(self) -> List[Order]:
        return [Order.get_from_xml(item) for item in self.get_results()]
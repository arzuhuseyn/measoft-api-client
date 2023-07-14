from typing import List
from xml.etree import ElementTree as ET

from entities import AbstractObject, Courier, Item, Package, Receiver, Sender, Status


class Order(AbstractObject):
    STATUSES = {
        "NEW": "Новый",
        "PICKUP": "Забран у отправителя",
        "ACCEPTED": "Получен складом",
        "INVENTORY": "Инвентаризация",
        "DEPARTURING": "Планируется отправка",
        "DEPARTURE": "Отправлено со склада",
        "DELIVERY": "Выдан курьеру на доставку",
        "COURIERDELIVERED": "Доставлен (предварительно)",
        "COMPLETE": "Доставлен",
        "PARTIALLY": "Доставлен частично",
        "COURIERRETURN": "Курьер вернул на склад",
        "CANCELED": "Не доставлен (Возврат/Отмена)",
        "RETURNING": "Планируется возврат",
        "RETURNED": "Возвращен",
        "CONFIRM": "Согласована доставка",
        "DATECHANGE": "Перенос",
        "NEWPICKUP": "Создан забор",
        "UNCONFIRM": "Не удалось согласовать доставку",
        "PICKUPREADY": "Готов к выдаче",
        "AWAITING_SYNC": "Ожидание синхронизации",
    }

    def __init__(
        self,
        order_number: str,
        awb: str,
        order_number2: str,
        order_code: str,
        given_code: str,
        barcode: str,
        sender: Sender,
        receiver: Receiver,
        weight: float,
        return_weight: float,
        quantity: int,
        pay_type: str,
        service: int,
        return_service: int,
        type: str,
        return_type: str,
        wait_time: str,
        price: float,
        print_check: bool,
        declared_price: float,
        enclosure: str,
        instruction: str,
        current_coordinates: dict,
        courier: Courier,
        delivery_price: dict,
        receiver_pays: bool,
        status: Status,
        status_history: List[Status],
        custom_state_code: str,
        client_state_code: str,
        delivered_to: str,
        delivered_date: str,
        delivered_time: str,
        external_system_code: str,
        items: List[Item],
        packages: List[Package],
    ):
        self.order_number = order_number
        self.awb = awb
        self.order_number2 = order_number2
        self.order_code = order_code
        self.given_code = given_code
        self.barcode = barcode
        self.sender = sender
        self.receiver = receiver
        self.weight = weight
        self.return_weight = return_weight
        self.quantity = quantity
        self.pay_type = pay_type
        self.service = service
        self.return_service = return_service
        self.type = type
        self.return_type = return_type
        self.wait_time = wait_time
        self.price = price
        self.print_check = print_check
        self.declared_price = declared_price
        self.enclosure = enclosure
        self.instruction = instruction
        self.current_coordinates = current_coordinates
        self.courier = courier
        self.delivery_price = delivery_price
        self.receiver_pays = receiver_pays
        self.status = status
        self.status_history = status_history
        self.custom_state_code = custom_state_code
        self.client_state_code = client_state_code
        self.delivered_to = delivered_to
        self.delivered_date = delivered_date
        self.delivered_time = delivered_time
        self.external_system_code = external_system_code
        self.items = items
        self.packages = packages

    @staticmethod
    def get_from_xml(xml: ET.Element, from_node: bool = True) -> "Order":
        params = {
            "order_number": Order.extract_xml_value(xml, "orderno", False),
            "awb": Order.extract_xml_value(xml, "awb", False),
            "order_number2": Order.extract_xml_value(xml, "orderno2", False),
            "order_code": Order.extract_xml_value(xml, "ordercode", False),
            "given_code": Order.extract_xml_value(xml, "givencode", False),
            "barcode": Order.extract_xml_value(xml, "barcode", True),
            "weight": Order.extract_xml_value(xml, "weight", True, "float"),
            "return_weight": Order.extract_xml_value(
                xml, "return_weight", True, "float"
            ),
            "quantity": Order.extract_xml_value(xml, "quantity", True, "int"),
            "pay_type": Order.extract_xml_value(xml, "paytype", True),
            "service": Order.extract_xml_value(xml, "service", True, "int"),
            "return_service": Order.extract_xml_value(
                xml, "return_service", True, "int"
            ),
            "type": Order.extract_xml_value(xml, "type", True),
            "return_type": Order.extract_xml_value(xml, "return_type", True),
            "wait_time": Order.extract_xml_value(xml, "waittime", True),
            "price": Order.extract_xml_value(xml, "price", True, "float"),
            "declared_price": Order.extract_xml_value(xml, "inshprice", True, "float"),
            "enclosure": Order.extract_xml_value(xml, "enclosure", True),
            "instruction": Order.extract_xml_value(xml, "instruction", True),
            "custom_state_code": Order.extract_xml_value(xml, "customstatecode", True),
            "client_state_code": Order.extract_xml_value(xml, "clientstatecode", True),
            "delivered_to": Order.extract_xml_value(xml, "deliveredto", True),
            "delivered_date": Order.extract_xml_value(xml, "delivereddate", True),
            "delivered_time": Order.extract_xml_value(xml, "deliveredtime", True),
            "external_system_code": Order.extract_xml_value(xml, "outstrbarcode", True),
            "print_check": True if xml.find("print_check") is not None else None,
            "receiver_pays": True if xml.find("receiverpays") is not None else None,
        }
        params["sender"] = (
            Sender.get_from_xml(xml.find("sender"))
            if xml.find("sender") is not None
            else None
        )
        params["receiver"] = (
            Receiver.get_from_xml(xml.find("receiver"))
            if xml.find("receiver") is not None
            else None
        )
        params["courier"] = (
            Courier.get_from_xml(xml.find("courier"))
            if xml.find("courier") is not None
            else None
        )
        params["status"] = (
            Status.get_from_xml(xml.find("status"), False)
            if xml.find("status") is not None
            else None
        )
        if xml.find("items") is not None:
            params["items"] = [
                Item.get_from_xml(order_item, False)
                for order_item in xml.find("items").getchildren()
            ]
        if xml.find("statushistory") is not None:
            params["status_history"] = [
                Status.get_from_xml(status_history, False)
                for status_history in xml.find("statushistory").getchildren()
            ]
        if xml.find("currcoords") is not None:
            params["current_coordinates"] = {
                "latitude": Order.extract_xml_value(
                    xml.find("currcoords"), "lat", False, "float"
                ),
                "longitude": Order.extract_xml_value(
                    xml.find("currcoords"), "lon", False, "float"
                ),
                "accuracy": Order.extract_xml_value(
                    xml.find("currcoords"), "accuracy", False, "float"
                ),
                "updated_at": Order.extract_xml_value(
                    xml.find("currcoords"), "RequestDateTime", False
                ),
            }
        if xml.find("deliveryprice") is not None:
            params["delivery_price"] = {
                "total": Order.extract_xml_value(
                    xml.find("deliveryprice"), "total", False, "float"
                ),
                "delivery": Order.extract_xml_value(
                    xml.find("deliveryprice"), "delivery", False, "float"
                ),
                "return": Order.extract_xml_value(
                    xml.find("deliveryprice"), "return", False, "float"
                ),
                "services": [],
            }
            for service in xml.find("deliveryprice").getchildren():
                params["delivery_price"]["services"].append(
                    {
                        "name": service.text,
                        "code": Order.extract_xml_value(
                            service, "code", False, "float"
                        ),
                        "price": Order.extract_xml_value(service, "price", False),
                    }
                )
        if xml.find("packages") is not None:
            params["packages"] = [
                Package.get_from_xml(package, False)
                for package in xml.find("packages").getchildren()
            ]

        return Order(**params)

    def __str__(self):
        return f"Order: {self.order_number}"

    def __repr__(self):
        return f"Order: {self.order_number}"

    def get_order_number(self) -> str:
        return self.order_number

    def get_awb(self) -> str:
        return self.awb

    def get_order_number2(self) -> str:
        return self.order_number2

    def get_order_code(self) -> str:
        return self.order_code

    def get_given_code(self) -> str:
        return self.given_code

    def get_barcode(self) -> str:
        return self.barcode

    def get_sender(self) -> Sender:
        return self.sender

    def get_receiver(self) -> Receiver:
        return self.receiver

    def get_weight(self) -> float:
        return self.weight

    def get_return_weight(self) -> float:
        return self.return_weight

    def get_quantity(self) -> int:
        return self.quantity

    def get_pay_type(self) -> str:
        return self.pay_type

    def get_service(self) -> int:
        return self.service

    def get_return_service(self) -> int:
        return self.return_service

    def get_type(self) -> str:
        return self.type

    def get_return_type(self) -> str:
        return self.return_type

    def get_wait_time(self) -> str:
        return self.wait_time

    def get_price(self) -> float:
        return self.price

    def get_print_check(self) -> bool:
        return self.print_check

    def get_declared_price(self) -> float:
        return self.declared_price

    def get_enclosure(self) -> str:
        return self.enclosure

    def get_instruction(self) -> str:
        return self.instruction

    def get_current_coordinates(self) -> dict:
        return self.current_coordinates

    def get_courier(self) -> Courier:
        return self.courier

    def get_delivery_price(self) -> dict:
        return self.delivery_price

    def get_receiver_pays(self) -> bool:
        return self.receiver_pays

    def get_status(self) -> Status:
        return self.status

    def get_status_history(self) -> List[Status]:
        return self.status_history

    def get_custom_state_code(self) -> str:
        return self.custom_state_code

    def get_client_state_code(self) -> str:
        return self.client_state_code

    def get_delivered_to(self) -> str:
        return self.delivered_to

    def get_delivered_date(self) -> str:
        return self.delivered_date

    def get_delivered_time(self) -> str:
        return self.delivered_time

    def get_external_system_code(self) -> str:
        return self.external_system_code

    def get_items(self) -> List[Item]:
        return self.items

    def get_packages(self) -> List[Package]:
        return self.packages

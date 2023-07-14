from xml.etree.ElementTree import Element as SimpleXMLElement

from operations import AbstractOperation, OrderSearchOperation
from api import MeasoftApi as Api
from entities import (
    Order,
    CreateOrderSender,
    CreateOrderReceiver,
    CreateOrderItem,
    CreateOrderPackage,
)


class CreateOrderOperation(AbstractOperation):
    def __init__(self, api: Api):
        super().__init__(api)
        self.new_folder = None
        self.order_number = None
        self.barcode = None
        self.sender = None
        self.receiver = None
        self.return_ = None
        self.weight = None
        self.return_weight = None
        self.quantity = None
        self.pay_type = None
        self.service = None
        self.return_service = None
        self.type = None
        self.return_type = None
        self.price = None
        self.delivery_price = None
        self.declared_price = None
        self.receiver_pays = None
        self.enclosure = None
        self.instruction = None
        self.department = None
        self.pickup = None
        self.accept_partially = None
        self.items = []
        self.packages = []
        self.delivery_set = None
        self.delivery_set_below_list = []

    def set_new_folder(self, new_folder: bool) -> "CreateOrderOperation":
        self.new_folder = "YES" if new_folder else "NO"
        return self

    def set_order_number(self, order_number: str) -> "CreateOrderOperation":
        self.order_number = order_number
        return self

    def set_barcode(self, barcode: str) -> "CreateOrderOperation":
        self.barcode = barcode
        return self

    def set_sender(self, sender: CreateOrderSender) -> "CreateOrderOperation":
        self.sender = sender
        return self

    def set_receiver(self, receiver: CreateOrderReceiver) -> "CreateOrderOperation":
        self.receiver = receiver
        return self

    def set_return(self, return_: bool) -> "CreateOrderOperation":
        self.return_ = "YES" if return_ else "NO"
        return self

    def set_weight(self, weight: float) -> "CreateOrderOperation":
        self.weight = weight
        return self

    def set_return_weight(self, return_weight: float) -> "CreateOrderOperation":
        self.return_weight = return_weight
        return self

    def set_quantity(self, quantity: int) -> "CreateOrderOperation":
        self.quantity = quantity
        return self

    def set_pay_type(self, pay_type: str) -> "CreateOrderOperation":
        if pay_type not in [
            self.PAYMENT_TYPE_CASH,
            self.PAYMENT_TYPE_CARD,
            self.PAYMENT_TYPE_NONE,
            self.PAYMENT_TYPE_OTHER,
        ]:
            raise Exception("Неверный способ оплаты")

        self.pay_type = pay_type
        return self

    def set_service(self, service: str) -> "CreateOrderOperation":
        self.service = service
        return self

    def set_return_service(self, return_service: str) -> "CreateOrderOperation":
        self.return_service = return_service
        return self

    def set_type(self, type_: str) -> "CreateOrderOperation":
        self.type = type_
        return self

    def set_return_type(self, return_type: str) -> "CreateOrderOperation":
        self.return_type = return_type
        return self

    def set_price(self, price: float) -> "CreateOrderOperation":
        self.price = price
        return self

    def set_delivery_price(self, delivery_price: float) -> "CreateOrderOperation":
        self.delivery_price = delivery_price
        return self

    def set_declared_price(self, declared_price: float) -> "CreateOrderOperation":
        self.declared_price = declared_price
        return self

    def set_receiver_pays(self, receiver_pays: bool) -> "CreateOrderOperation":
        self.receiver_pays = "YES" if receiver_pays else "NO"
        return self

    def set_enclosure(self, enclosure: str) -> "CreateOrderOperation":
        self.enclosure = enclosure
        return self

    def set_instruction(self, instruction: str) -> "CreateOrderOperation":
        self.instruction = instruction
        return self

    def set_department(self, department: str) -> "CreateOrderOperation":
        self.department = department
        return self

    def set_pickup(self, pickup: bool) -> "CreateOrderOperation":
        self.pickup = "YES" if pickup else "NO"
        return self

    def set_accept_partially(self, accept_partially: bool) -> "CreateOrderOperation":
        self.accept_partially = "YES" if accept_partially else "NO"
        return self

    def add_item(self, item: CreateOrderItem) -> "CreateOrderOperation":
        self.items.append(item)
        return self

    def add_package(self, package: CreateOrderPackage) -> "CreateOrderOperation":
        self.packages.append(package)
        return self

    def set_delivery_set(
        self, above_price: float, return_price: float
    ) -> "CreateOrderOperation":
        self.delivery_set = {
            "above_price": above_price,
            "return_price": return_price,
        }
        return self

    def add_delivery_set_below(
        self, sum_: float, price: float
    ) -> "CreateOrderOperation":
        self.delivery_below_list.append(
            {
                "sum": sum_,
                "price": price,
            }
        )
        return self

    def build_xml(self) -> SimpleXMLElement:
        xml = self.create_xml("neworder")
        order = xml.add_child("order")
        order_items = order.add_child("items")
        sender = order.add_child("sender")
        receiver = order.add_child("receiver")
        order_packages = order.add_child("packages")

        xml.set("newfolder", self.new_folder)

        order.set("orderno", self.order_number)
        order.add_child("barcode", self.barcode)
        order.add_child("return", self.return_)
        order.add_child("weight", self.weight)
        order.add_child("return_weight", self.return_weight)
        order.add_child("quantity", self.quantity)
        order.add_child("paytype", self.pay_type)
        order.add_child("service", self.service)
        order.add_child("return_service", self.return_service)
        order.add_child("type", self.type)
        order.add_child("return_type", self.return_type)
        order.add_child("price", self.price)
        order.add_child("deliveryprice", self.delivery_price)
        order.add_child("inshprice", self.declared_price)
        order.add_child("receiverpays", self.receiver_pays)
        order.add_child("enclosure", self.enclosure)
        order.add_child("instruction", self.instruction)
        order.add_child("department", self.department)
        order.add_child("pickup", self.pickup)
        order.add_child("acceptpartially", self.accept_partially)

        if self.sender:
            sender.add_child("company", self.sender.company)
            sender.add_child("person", self.sender.person)
            sender.add_child("phone", self.sender.phone)
            sender.add_child("town", self.sender.town)
            sender.add_child("address", self.sender.address)
            sender.add_child("date", self.sender.date)
            sender.add_child("time_min", self.sender.time_min)
            sender.add_child("time_max", self.sender.time_max)

        if self.receiver:
            receiver.add_child("company", self.receiver.company)
            receiver.add_child("person", self.receiver.person)
            receiver.add_child("phone", self.receiver.phone)
            receiver.add_child("zipcode", self.receiver.zipcode)
            receiver.add_child("address", self.receiver.address)
            receiver.add_child("pvz", self.receiver.pvz_code)
            receiver.add_child("date", self.receiver.date)
            receiver.add_child("time_min", self.receiver.time_min)
            receiver.add_child("time_max", self.receiver.time_max)
            town = receiver.add_child("town", self.receiver.town)
            town.add_child("regioncode", self.receiver.region_code)

        for item in self.items:
            order_item = order_items.add_child("item", item.name)
            order_item.set("extcode", item.external_code)
            order_item.set("quantity", item.quantity)
            order_item.set("mass", item.weight)
            order_item.set("retprice", item.retail_price)
            order_item.set("VATrate", item.vat_rate)
            order_item.set("barcode", item.barcode)
            order_item.set("article", item.article)
            order_item.set("volume", item.volume)
            order_item.set("type", item.type)
            order_item.set("length", item.length)
            order_item.set("width", item.width)
            order_item.set("height", item.height)

        for package in self.packages:
            order_package = order_packages.add_child("package", package.name)
            order_package.set("code", package.code)
            order_package.set("strbarcode", package.barcode)
            order_package.set("mass", package.weight)
            order_package.set("message", package.message)
            order_package.set("length", package.length)
            order_package.set("width", package.width)
            order_package.set("height", package.height)

        if self.delivery_set:
            delivery_set = order.add_child("deliveryset")
            delivery_set.set("above_price", self.delivery_set["above_price"])
            delivery_set.set("return_price", self.delivery_set["return_price"])

            for below in self.delivery_set_below_list:
                delivery_set_below = delivery_set.add_child("below")
                delivery_set_below.set("below_sum", below["sum"])
                delivery_set_below.set("price", below["price"])

        return xml

    def create(self) -> Order:
        for item in self.get_results():
            error_code = int(item.get("error", 0))

            if error_code:
                raise Exception(
                    item.get(
                        "errormsgru",
                        item.get("errormsg", "Код ошибки: {}".format(error_code)),
                    )
                )

            order = (
                OrderSearchOperation(self.api).order_number(item["orderno"]).search()[0]
                or None
            )

            if not order:
                raise Exception("Не удалось получить заказ")

            return order

        raise Exception("Неизвестная ошибка")

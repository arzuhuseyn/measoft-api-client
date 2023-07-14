from xml.etree import ElementTree as ET


class CreateOrderItem:
    def __init__(
        self,
        article: str,
        barcode: str,
        name: str,
        retail_price: float,
        weight: float,
        length: float,
        width: float,
        height: float,
        quantity: int,
        external_code: str,
        vat_rate: int,
        volume: float,
        type: int,
    ):
        self.article = article
        self.barcode = barcode
        self.name = name
        self.retail_price = retail_price
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.quantity = quantity
        self.external_code = external_code
        self.vat_rate = vat_rate
        self.volume = volume
        self.type = type
from xml.etree import ElementTree as ET

from entities.abstract_object import AbstractObject


class Item(AbstractObject):
    def __init__(
        self,
        name: str,
        code: str = None,
        article: str = None,
        barcode: str = None,
        retail_price: float = None,
        purchase_price: float = None,
        weight: float = None,
        length: float = None,
        width: float = None,
        height: float = None,
        count_in_pallet: int = None,
        has_serials: bool = None,
        country_of_origin: str = None,
        comment: str = None,
        comment2: str = None,
        quantity: int = None,
        reserved_quantity: int = None,
        external_code: str = None,
        vat_rate: int = None,
        returns: int = None,
    ):
        self.name = name
        self.code = code
        self.article = article
        self.barcode = barcode
        self.retail_price = retail_price
        self.purchase_price = purchase_price
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.count_in_pallet = count_in_pallet
        self.has_serials = has_serials
        self.country_of_origin = country_of_origin
        self.comment = comment
        self.comment2 = comment2
        self.quantity = quantity
        self.reserved_quantity = reserved_quantity
        self.external_code = external_code
        self.vat_rate = vat_rate
        self.returns = returns

    @staticmethod
    def get_from_xml(xml: ET.Element, from_node: bool = True) -> "Item":
        params = {
            "name": Item.extract_xml_value(xml, "name", from_node),
            "code": Item.extract_xml_value(xml, "code", from_node),
            "article": Item.extract_xml_value(xml, "article", from_node),
            "barcode": Item.extract_xml_value(xml, "barcode", from_node),
            "retail_price": Item.extract_xml_value(xml, "retprice", from_node, float),
            "purchase_price": Item.extract_xml_value(
                xml, "purchprice", from_node, float
            ),
            "weight": Item.extract_xml_value(
                xml, {"node": "weight", "attr": "mass"}, from_node, float
            ),
            "length": Item.extract_xml_value(xml, "length", from_node, float),
            "width": Item.extract_xml_value(xml, "width", from_node, float),
            "height": Item.extract_xml_value(xml, "height", from_node, float),
            "count_in_pallet": Item.extract_xml_value(
                xml, "CountInPallet", from_node, int
            ),
            "has_serials": Item.extract_xml_value(xml, "HasSerials", from_node, bool),
            "country_of_origin": Item.extract_xml_value(
                xml, "CountryOfOrigin", from_node
            ),
            "comment": Item.extract_xml_value(xml, "Message", from_node),
            "comment2": Item.extract_xml_value(xml, "Message2", from_node),
            "quantity": Item.extract_xml_value(xml, "quantity", from_node, int),
            "reserved_quantity": Item.extract_xml_value(
                xml, "reserved", from_node, int
            ),
            "external_code": Item.extract_xml_value(xml, "extcode", from_node),
            "vat_rate": Item.extract_xml_value(xml, "VATrate", from_node, int),
            "returns": Item.extract_xml_value(xml, "returns", from_node, int),
        }
        return Item(**params)

    def get_name(self) -> str:
        return self.name

    def get_code(self) -> str:
        return self.code

    def get_article(self) -> str:
        return self.article

    def get_barcode(self) -> str:
        return self.barcode

    def get_retail_price(self) -> float:
        return self.retail_price

    def get_purchase_price(self) -> float:
        return self.purchase_price

    def get_weight(self) -> float:
        return self.weight

    def get_length(self) -> float:
        return self.length

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def get_count_in_pallet(self) -> int:
        return self.count_in_pallet

    def get_has_serials(self) -> bool:
        return self.has_serials

    def get_country_of_origin(self) -> str:
        return self.country_of_origin

    def get_comment(self) -> str:
        return self.comment

    def get_comment2(self) -> str:
        return self.comment2

    def get_quantity(self) -> int:
        return self.quantity

    def get_reserved_quantity(self) -> int:
        return self.reserved_quantity

    def get_external_code(self) -> str:
        return self.external_code

    def get_vat_rate(self) -> int:
        return self.vat_rate

    def get_returns(self) -> int:
        return self.returns

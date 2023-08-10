from typing import List, Optional
from xml.etree.ElementTree import Element as SimpleXMLElement


from operations import AbstractOperation
from api import MeasoftApi as Api
from operations.traits import Limitable
from entities import Item


class ItemSearchOperation(AbstractOperation, Limitable):
    def __init__(self, api: Api):
        super().__init__(api)
        self.code: Optional[str] = None
        self.article: Optional[str] = None
        self.barcode: Optional[str] = None
        self.name_contains: Optional[str] = None
        self.name_starts: Optional[str] = None
        self.name: Optional[str] = None
        self.in_stock: Optional[bool] = None

    def code(self, code: str) -> "ItemSearchOperation":
        self.code = code
        return self

    def article(self, article: str) -> "ItemSearchOperation":
        self.article = article
        return self

    def barcode(self, barcode: str) -> "ItemSearchOperation":
        self.barcode = barcode
        return self

    def name_contains(self, name_contains: str) -> "ItemSearchOperation":
        self.name_contains = name_contains
        return self

    def name_starts(self, name_starts: str) -> "ItemSearchOperation":
        self.name_starts = name_starts
        return self

    def name(self, name: str) -> "ItemSearchOperation":
        self.name = name
        return self

    def in_stock(self, in_stock: Optional[bool]) -> "ItemSearchOperation":
        self.in_stock = in_stock
        return self

    def build_xml(self) -> SimpleXMLElement:
        xml = self.create_xml("itemlist")
        codesearch = xml.add_child("codesearch")
        conditions = xml.add_child("conditions")

        codesearch.add_child("code", self.code)
        codesearch.add_child("article", self.article)
        codesearch.add_child("barcode", self.barcode)

        conditions.add_child("namecontains", self.name_contains)
        conditions.add_child("namestarts", self.name_starts)
        conditions.add_child("name", self.name)
        conditions.add_child(
            "quantity",
            "EXISTING_ONLY"
            if self.in_stock
            else "NOT_EXISTING_ONLY"
            if self.in_stock is False
            else "ALL",
        )

        xml = self.build_limit_xml(xml)

        return xml

    def search(self) -> List[Item]:
        return [Item.get_from_xml(item) for item in self.get_results()]

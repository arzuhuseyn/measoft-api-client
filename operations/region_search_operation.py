from typing import List
from xml.etree.ElementTree import Element

from operations import AbstractOperation
from api import MeasoftApi as Api
from entities import Region


class RegionSearchOperation(AbstractOperation):
    def __init__(self, api: Api):
        super().__init__(api)
        self.code: str = None
        self.name_contains: str = None
        self.name_starts: str = None
        self.full_name: str = None
        self.country_code: str = None

    def code(self, code: str) -> "RegionSearchOperation":
        self.code = code
        return self

    def name_contains(self, name_contains: str) -> "RegionSearchOperation":
        self.name_contains = name_contains
        return self

    def name_starts(self, name_starts: str) -> "RegionSearchOperation":
        self.name_starts = name_starts
        return self

    def full_name(self, full_name: str) -> "RegionSearchOperation":
        self.full_name = full_name
        return self

    def country_code(self, country_code: str) -> "RegionSearchOperation":
        self.country_code = country_code
        return self

    def build_xml(self) -> Element:
        xml = self.create_xml("regionlist")
        codesearch = xml.add_child("codesearch")
        conditions = xml.add_child("conditions")
        codesearch.add_child("code", self.code)
        conditions.add_child("namecontains", self.name_contains)
        conditions.add_child("namestarts", self.name_starts)
        conditions.add_child("fullname", self.full_name)
        conditions.add_child("country", self.country_code)

        return xml

    def search(self) -> List[Region]:
        result = []
        for item in self.get_results(False):
            result.append(Region.get_from_xml(item))

        return result

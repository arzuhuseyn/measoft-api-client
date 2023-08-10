from typing import List
from xml.etree.ElementTree import Element as SimpleXMLElement

from api import MeasoftApi as Api
from operations import AbstractOperation
from operations.traits import Limitable
from entities import Town


class TownSearchOperation(AbstractOperation, Limitable):
    def __init__(self, api: Api):
        super().__init__(api)
        self.zipCode = None
        self.kladrCode = None
        self.fiasCode = None
        self.code = None
        self.regionName = None
        self.nameContains = None
        self.nameStarts = None
        self.name = None
        self.fullName = None
        self.countryCode = None

    def zipCode(self, zipCode: str):
        self.zipCode = zipCode
        return self

    def kladrCode(self, kladrCode: str):
        self.kladrCode = kladrCode
        return self

    def fiasCode(self, fiasCode: str):
        self.fiasCode = fiasCode
        return self

    def code(self, code: str):
        self.code = code
        return self

    def regionName(self, regionName: str):
        self.regionName = regionName
        return self

    def nameContains(self, nameContains: str):
        self.nameContains = nameContains
        return self

    def nameStarts(self, nameStarts: str):
        self.nameStarts = nameStarts
        return self

    def name(self, name: str):
        self.name = name
        return self

    def fullName(self, fullName: str):
        self.fullName = fullName
        return self

    def countryCode(self, countryCode: str):
        self.countryCode = countryCode
        return self

    def buildXml(self) -> SimpleXMLElement:
        xml = self.create_xml("townlist")
        codesearch = xml.addChild("codesearch")
        conditions = xml.addChild("conditions")

        codesearch.addChild("zipcode", self.zipCode)
        codesearch.addChild("kladrcode", self.kladrCode)
        codesearch.addChild("fiascode", self.fiasCode)
        codesearch.addChild("code", self.code)

        conditions.addChild("region", self.regionName)
        conditions.addChild("namecontains", self.nameContains)
        conditions.addChild("namestarts", self.nameStarts)
        conditions.addChild("name", self.name)
        conditions.addChild("fullname", self.fullName)
        conditions.addChild("country", self.countryCode)

        self.build_limit_xml(xml)

        return xml

    def search(self) -> List[Town]:
        result = []
        for item in self.getResults(False):
            result.append(Town.getFromXml(item))
        return result

from xml.etree.ElementTree import Element as SimpleXMLElement

from entities.abstract_object import AbstractObject
from entities.region import Region


class Town(AbstractObject):
    def __init__(
        self, code: str, name: str, fiasCode: str, kladrCode: str, region: Region
    ):
        self.code = code
        self.name = name
        self.fiasCode = fiasCode
        self.kladrCode = kladrCode
        self.region = region

    @staticmethod
    def get_from_xml(xml: SimpleXMLElement, from_node: bool = True) -> Town:
        if "city" in xml:
            region = Region.get_from_xml(xml.city)
        elif "regioncode" in xml:
            region = Region(
                code=str(xml["regioncode"]),
                name=str(xml["regionname"] if "regionname" in xml else ""),
            )

        return Town(
            code=xml.code if from_node else str(xml),
            name=xml.name if from_node else str(xml),
            fiasCode=xml.fiascode if from_node else str(xml),
            kladrCode=xml.kladrcode if from_node else str(xml),
            region=region,
        )

    def get_code(self) -> str:
        return self.code

    def set_code(self, code: str) -> "Town":
        self.code = code
        return self

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> "Town":
        self.name = name
        return self

    def get_fias_code(self) -> str:
        return self.fiasCode

    def get_kladr_code(self) -> str:
        return self.kladrCode

    def get_region(self) -> Region:
        return self.region

    def set_region(self, region: Region) -> "Town":
        self.region = region
        return self

    def __str__(self) -> str:
        return self.name

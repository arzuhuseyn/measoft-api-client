from xml.etree import ElementTree as ET

from entities.abstract_object import AbstractObject


class Package(AbstractObject):
    def __init__(
        self,
        name: str,
        code: str,
        barcode: str,
        message: str,
        weight: float,
        length: float,
        width: float,
        height: float,
    ):
        self.name = name
        self.code = code
        self.barcode = barcode
        self.message = message
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height

    @staticmethod
    def get_from_xml(xml: ET.Element, from_node: bool = True) -> "Package":
        params = {
            "name": Package.extract_xml_value(xml, "name", from_node),
            "code": Package.extract_xml_value(xml, "code", from_node),
            "barcode": Package.extract_xml_value(xml, "strbarcode", from_node),
            "message": Package.extract_xml_value(xml, "message", from_node),
            "weight": Package.extract_xml_value(xml, "mass", from_node, "float"),
            "length": Package.extract_xml_value(xml, "length", from_node, "float"),
            "width": Package.extract_xml_value(xml, "width", from_node, "float"),
            "height": Package.extract_xml_value(xml, "height", from_node, "float"),
        }

        return Package(**params)

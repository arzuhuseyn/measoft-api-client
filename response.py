from typing import Optional
from xml.etree.ElementTree import Element as SimpleXMLElement


class Response:
    def __init__(self, success: bool, xml: Optional[SimpleXMLElement] = None, error: Optional[str] = None):
        self.success = success
        self.xml = xml
        self.error = error

    def is_success(self) -> bool:
        return self.success

    def get_xml(self) -> SimpleXMLElement:
        return self.xml

    def get_error(self) -> Optional[str]:
        return self.error
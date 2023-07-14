from xml.etree.ElementTree import Element as SimpleXMLElement
from xml.etree.ElementTree import fromstring

from api import MeasoftApi as Api
from response import Response


class AbstractOperation:
    def __init__(self, api: Api):
        self.api = api
        self.responses = []

    def get_last_response(self) -> Response:
        return self.responses[-1] if self.responses else None

    def create_xml(self, start_tag: str) -> SimpleXMLElement:
        return fromstring(f'<?xml version="1.0" encoding="UTF-8"?><{start_tag}/>')

    def remove_empty_xml_nodes(self, xml: SimpleXMLElement):
        xpath = "/child::*//*[not(*) and not(@*) and not(text()[normalize-space()])]"
        end = False

        while end is False:
            end = True

            for node in xml.xpath(xpath):
                del node[0]
                end = False

    def remove_empty_xml_attributes(self, xml: SimpleXMLElement):
        xpath = "//*[@*]"
        empty_attr_names = []

        for node in xml.xpath(xpath):
            attrs = node.attributes()

            for name, value in attrs.items():
                if str(value) == "":
                    empty_attr_names.append(name)

            for name in empty_attr_names:
                del attrs[name]

    def request(self, xml: SimpleXMLElement, with_auth: bool = True) -> Response:
        self.remove_empty_xml_nodes(xml)
        self.remove_empty_xml_attributes(xml)
        response = self.api.request(xml, with_auth)
        self.responses.append(response)
        return response

    def build_xml(self):
        raise NotImplementedError

    def get_results(self, with_auth: bool = True) -> SimpleXMLElement:
        response = self.request(self.build_xml(), with_auth)

        if not response.is_success():
            raise Exception(response.get_error())

        return response.get_xml()

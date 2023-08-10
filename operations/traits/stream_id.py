from xml.etree.ElementTree import Element


class StreamId:
    def __init__(self):
        self.stream_id = None

    def stream_id(self, stream_id) -> "StreamId":
        self.stream_id = stream_id
        return self

    def build_stream_id_xml(self, xml: Element) -> Element:
        xml.append(self.create_xml_element("streamid", self.stream_id))
        return xml

    def create_xml_element(self, name, value) -> str:
        element = Element(name)
        element.text = str(value)
        return element
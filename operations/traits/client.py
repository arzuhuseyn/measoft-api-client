from xml.etree.ElementTree import Element


class Client:
    def __init__(self):
        self.client = None

    def client(self, client: bool = True) -> "Client":
        self.client = "CLIENT" if client else "AGENT"
        return self

    def build_client_xml(self, xml: Element):
        xml.add_child("client", self.client)
        return xml
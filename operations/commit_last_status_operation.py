from operations import AbstractOperation


class CommitLastStatusOperation(AbstractOperation):
    def __init__(self, api):
        super().__init__(api)
        self.stream_id = None

    def stream_id(self, stream_id) -> "CommitLastStatusOperation":
        self.stream_id = stream_id
        return self

    def commit(self):
        xml = self.get_results()

        error_code = int(xml.get("error", 0))

        if error_code:
            raise Exception(
                xml.get("errormsgru")
                or xml.get("errormsg")
                or f"Код ошибки: {error_code}"
            )

    def build_xml(self):
        xml = self.create_xml("commitlaststatus")
        xml.append(self.create_xml_element("streamid", self.stream_id))

        return xml

from typing import Optional, Union
from xml.etree.ElementTree import Element as SimpleXMLElement


class AbstractObject:
    def __init__(self, properties: dict = None):
        if properties is None:
            properties = {}
        for property, value in properties.items():
            if hasattr(self, property) and value is not None:
                setattr(self, property, value)

    @staticmethod
    def extract_xml_value(
        xml: Optional[SimpleXMLElement],
        key: Union[str, dict],
        from_node: bool = True,
        type: str = "string",
    ) -> Optional[Union[bool, float, int, str]]:
        if xml is None:
            return None
        key = key["node" if from_node else "attr"] if isinstance(key, dict) else key
        value = xml[key] if from_node else xml[key]
        if value is None:
            return None
        if type == "string":
            value = str(value)
        elif type == "int":
            value = int(value)
        elif type == "float":
            value = float(value)
        elif type == "bool":
            value = bool(value)
        else:
            raise Exception("Неверно указан тип переменной")
        return value

    def json_serialize(self) -> dict:
        return vars(self)
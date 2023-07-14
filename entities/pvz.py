from xml.etree import ElementTree as ET

from entities.abstract_object import AbstractObject
from entities.town import Town


class Pvz(AbstractObject):
    def __init__(
        self,
        code: str = None,
        clientCode: str = None,
        name: str = None,
        parentCode: str = None,
        parentName: str = None,
        town: Town = None,
        address: str = None,
        phone: str = None,
        comment: str = None,
        workTime: str = None,
        travelDescription: str = None,
        maxWeight: float = None,
        acceptCash: bool = None,
        acceptCard: bool = None,
        acceptFitting: bool = None,
        acceptIndividuals: bool = None,
        latitude: float = None,
        longitude: float = None,
    ):
        self.code = code
        self.clientCode = clientCode
        self.name = name
        self.parentCode = parentCode
        self.parentName = parentName
        self.town = town
        self.address = address
        self.phone = phone
        self.comment = comment
        self.workTime = workTime
        self.travelDescription = travelDescription
        self.maxWeight = maxWeight
        self.acceptCash = acceptCash
        self.acceptCard = acceptCard
        self.acceptFitting = acceptFitting
        self.acceptIndividuals = acceptIndividuals
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def get_from_xml(xml: ET.Element, from_node: bool = True) -> "Pvz":
        if xml.find("town") is not None:
            town = Town.get_from_xml(xml.find("town"), False)
        else:
            town = None

        return Pvz(
            code=xml.findtext("code") if from_node else xml.get("code"),
            clientCode=xml.findtext("clientcode")
            if from_node
            else xml.get("clientcode"),
            name=xml.findtext("name") if from_node else xml.get("name"),
            parentCode=xml.findtext("parentcode")
            if from_node
            else xml.get("parentcode"),
            parentName=xml.findtext("parentname")
            if from_node
            else xml.get("parentname"),
            address=xml.findtext("address") if from_node else xml.get("address"),
            phone=xml.findtext("phone") if from_node else xml.get("phone"),
            comment=xml.findtext("comment") if from_node else xml.get("comment"),
            workTime=xml.findtext("worktime") if from_node else xml.get("worktime"),
            travelDescription=xml.findtext("traveldescription")
            if from_node
            else xml.get("traveldescription"),
            maxWeight=float(xml.findtext("maxweight"))
            if from_node
            else float(xml.get("maxweight")),
            latitude=float(xml.findtext("latitude"))
            if from_node
            else float(xml.get("latitude")),
            longitude=float(xml.findtext("longitude"))
            if from_node
            else float(xml.get("longitude")),
            acceptCash=xml.findtext("acceptcash") == "YES"
            if from_node
            else xml.get("acceptcash") == "YES",
            acceptCard=xml.findtext("acceptcard") == "YES"
            if from_node
            else xml.get("acceptcard") == "YES",
            acceptFitting=xml.findtext("acceptfitting") == "YES"
            if from_node
            else xml.get("acceptfitting") == "YES",
            acceptIndividuals=xml.findtext("acceptindividuals") == "YES"
            if from_node
            else xml.get("acceptindividuals") == "YES",
            town=town,
        )

    def __str__(self):
        return "%s (%s)" % (self.name, self.code)

    def __repr__(self):
        return "<Measoft Pvz %s>" % self.__str__()

    def __eq__(self, other):
        if isinstance(other, Pvz):
            return self.code == other.code
        return False

    def __hash__(self):
        return hash(self.code)

    def get_code(self) -> str:
        return self.code

    def get_client_code(self) -> str:
        return self.clientCode

    def get_name(self) -> str:
        return self.name

    def get_parent_code(self) -> str:
        return self.parentCode

    def get_parent_name(self) -> str:
        return self.parentName

    def get_town(self) -> Town:
        return self.town

    def get_address(self) -> str:
        return self.address

    def get_phone(self) -> str:
        return self.phone

    def get_comment(self) -> str:
        return self.comment

    def get_work_time(self) -> str:
        return self.workTime

    def get_travel_description(self) -> str:
        return self.travelDescription

    def get_max_weight(self) -> float:
        return self.maxWeight

    def get_accept_cash(self) -> bool:
        return self.acceptCash

    def get_accept_card(self) -> bool:
        return self.acceptCard

    def get_accept_fitting(self) -> bool:
        return self.acceptFitting

    def get_accept_individuals(self) -> bool:
        return self.acceptIndividuals

    def get_latitude(self) -> float:
        return self.latitude

    def get_longitude(self) -> float:
        return self.longitude

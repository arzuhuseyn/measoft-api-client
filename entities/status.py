from typing import List
from xml.etree import ElementTree as ET

from entities.abstract_object import AbstractObject
from entities.country import Country


class Status(AbstractObject):
    STATUS_AWAITING_SYNC = "AWAITING_SYNC"
    STATUS_NEW = "NEW"
    STATUS_NEWPICKUP = "NEWPICKUP"
    STATUS_PICKUP = "PICKUP"
    STATUS_WMSASSEMBLED = "WMSASSEMBLED"
    STATUS_WMSDISASSEMBLED = "WMSDISASSEMBLED"
    STATUS_ACCEPTED = "ACCEPTED"
    STATUS_CUSTOMSPROCESS = "CUSTOMSPROCESS"
    STATUS_CUSTOMSFINISHED = "CUSTOMSFINISHED"
    STATUS_CONFIRM = "CONFIRM"
    STATUS_UNCONFIRM = "UNCONFIRM"
    STATUS_DEPARTURING = "DEPARTURING"
    STATUS_DEPARTURE = "DEPARTURE"
    STATUS_INVENTORY = "INVENTORY"
    STATUS_PICKUPREADY = "PICKUPREADY"
    STATUS_DELIVERY = "DELIVERY"
    STATUS_COURIERDELIVERED = "COURIERDELIVERED"
    STATUS_COURIERPARTIALLY = "COURIERPARTIALLY"
    STATUS_COURIERCANCELED = "COURIERCANCELED"
    STATUS_COURIERRETURN = "COURIERRETURN"
    STATUS_DATECHANGE = "DATECHANGE"
    STATUS_COMPLETE = "COMPLETE"
    STATUS_PARTIALLY = "PARTIALLY"
    STATUS_CANCELED = "CANCELED"
    STATUS_RETURNING = "RETURNING"
    STATUS_RETURNED = "RETURNED"
    STATUS_LOST = "LOST"
    STATUS_PARTLYRETURNING = "PARTLYRETURNING"
    STATUS_PARTLYRETURNED = "PARTLYRETURNED"
    STATUS_TRANSACCEPTED = "TRANSACCEPTED"
    STATUS_PICKUPTRANS = "PICKUPTRANS"

    def __init__(
        self,
        name: str,
        eventStore: str,
        eventTime: str,
        createTimeGmt: str,
        message: str,
        title: str,
    ):
        self.name = name
        self.eventStore = eventStore
        self.eventTime = eventTime
        self.createTimeGmt = createTimeGmt
        self.message = message
        self.title = title

    @staticmethod
    def get_from_xml(xml: ET.Element, from_node: bool = True) -> "Status":
        params = {
            "name": Status.extract_xml_value(xml, "name", from_node),
            "eventStore": Status.extract_xml_value(xml, "eventstore", from_node),
            "eventTime": Status.extract_xml_value(xml, "eventtime", from_node),
            "createTimeGmt": Status.extract_xml_value(xml, "createtimegmt", from_node),
            "message": Status.extract_xml_value(xml, "message", from_node),
            "title": Status.extract_xml_value(xml, "title", from_node),
        }

        return Status(**params)

    def is_delivered(self) -> bool:
        return self.name == "COMPLETE"

    def is_delivered_partially(self) -> bool:
        return self.name in ["PARTIALLY", "PARTLYRETURNING", "PARTLYRETURNED"]

    def is_cancelled(self) -> bool:
        return self.name in ["CANCELED", "RETURNING", "RETURNED"]

    def is_returned(self) -> bool:
        return self.name in ["RETURNED", "PARTLYRETURNED"]

from typing import List

from api import MeasoftApi as Api
from entities.country import Country

from operations import (
    RegionSearchOperation,
    TownSearchOperation,
    StreetSearchOperation,
    PvzSearchOperation,
    ItemSearchOperation,
    CalculatorOperation,
    OrderSearchOperation,
    CreateOrderOperation,
    CancelOrderOperation,
    CommitLastStatusOperation,
)


class MeasoftClient:
    def __init__(self, login: str, password: str, extracode: str):
        self.api = Api(login, password, extracode)

    def get_country_list(self) -> List[Country]:
        countries = {}
        for region in self.region_search().search():
            countries[region.country.code] = region.country
        return list(countries.values())

    def region_search(self) -> RegionSearchOperation:
        return RegionSearchOperation(self.api)

    def town_search(self) -> TownSearchOperation:
        return TownSearchOperation(self.api)

    def street_search(self) -> StreetSearchOperation:
        return StreetSearchOperation(self.api)

    def pvz_search(self) -> PvzSearchOperation:
        return PvzSearchOperation(self.api)

    def item_search(self) -> ItemSearchOperation:
        return ItemSearchOperation(self.api)

    def calculator(self) -> CalculatorOperation:
        return CalculatorOperation(self.api)

    def order_search(self) -> OrderSearchOperation:
        return OrderSearchOperation(self.api)

    def create_order(self) -> CreateOrderOperation:
        return CreateOrderOperation(self.api)

    def cancel_order(self) -> CancelOrderOperation:
        return CancelOrderOperation(self.api)

    def commit_last_status(self) -> CommitLastStatusOperation:
        return CommitLastStatusOperation(self.api)

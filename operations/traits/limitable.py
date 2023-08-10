from xml.etree.ElementTree import Element


class Limitable:
    def __init__(self):
        self.offset = 0
        self.limit = 10000
        self.count_all = False

    def offset(self, offset: int) -> "Limitable":
        self.offset = offset
        return self

    def limit(self, limit: int) -> "Limitable":
        self.limit = limit
        return self

    def count_all(self, count_all: bool = True) -> "Limitable":
        self.count_all = count_all
        return self

    def build_limit_xml(self, xml: Element):
        limit = xml.add_child("limit")

        if limit:
            limit.add_child("limitfrom", self.offset)
            limit.add_child("limitcount", self.limit)
            limit.add_child("countall", "YES" if self.count_all else None)
        
        return xml



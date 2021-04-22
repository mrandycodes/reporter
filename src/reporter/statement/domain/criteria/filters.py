from .filter import Filter


class Filters:
    def __init__(self):
        self.filters = []

    def add(self, filter_item: Filter):
        self.filters.append(filter_item)

    def count(self) -> int:
        return len(self.filters)

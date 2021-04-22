from .filters import Filters


class Criteria:
    def __init__(self, filters: Filters, limit: int = None):
        self.filters = filters
        self.limit = limit

    def has_filters(self) -> bool:
        return self.filters.count() > 0

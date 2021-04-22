from .filter_field import FilterField
from .filter_operator import FilterOperator
from .filter_value import FilterValue


class Filter:
    def __init__(self, field: FilterField, operator: FilterOperator, value: FilterValue):
        self.field = field
        self.operator = operator
        self.value = value

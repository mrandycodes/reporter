from src.reporter.statement.domain.criteria.criteria import Criteria
import requests


class FinancialModelingPrepApi:
    @staticmethod
    def find_by_criteria(criteria: Criteria):
        if not criteria.has_filters():
            return None

        company_name = ''
        variables = {}

        for filter_item in criteria.filters:
            if filter_item.field == "company_name":
                company_name = filter_item.value
                continue

            variables[filter_item.field] = filter_item.value

        if criteria.limit is not None:
            variables["limit"] = criteria.limit

        variables["apiKey"] = 'demo'
        uri = 'https://financialmodelingprep.co' + '/' + company_name

        resp = requests.get(uri, params=variables)

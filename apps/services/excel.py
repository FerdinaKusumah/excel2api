import ssl

import pandas

from apps.abstracts import AbstractExcelToApi
from apps.helpers import cache

# unblocking checking certs https
ssl._create_default_https_context = ssl._create_unverified_context


class Excel(AbstractExcelToApi):

    def __init__(self):
        AbstractExcelToApi.__init__(self)

    @cache(ttl=360)
    def fetch_excel(self, sheet_name: str = None, sheet_url: str = None) -> dict:
        """Fetch data excel from url
        :param sheet_name: str
        :param sheet_url: str
        :return: dict
        """
        return pandas.read_excel(sheet_url, sheet_name=sheet_name).to_json(orient='records')

    @cache(ttl=360)
    def fetch_csv(self, file_url: str = None) -> dict:
        """Fetch data excel from url
        :param file_url: str
        :return: dict
        """
        return pandas.read_csv(file_url).to_json(orient='records')

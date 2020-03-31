from abc import ABC, abstractmethod


class ExcelToApi(ABC):

    @abstractmethod
    def fetch_excel(self, sheet_name: str = None, sheet_url: str = None) -> dict:
        """Fetch data excel from url
        :param sheet_name: str
        :param sheet_url: str
        :return: dict
        """
        pass

    @abstractmethod
    def fetch_csv(self, file_url: str = None) -> dict:
        """Fetch data excel from url
        :param file_url: str
        :return: dict
        """
        pass

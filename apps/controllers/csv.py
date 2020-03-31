import orjson

from apps.services import ExcelServiceApi


class CsvController(ExcelServiceApi):

    def __init__(self):
        ExcelServiceApi.__init__(self)

    def fetch(self, sheet_url: str, row_range: str, column_range: str) -> dict:
        """Convert all data from pandas to dictionary
        :param sheet_url: str
        :param row_range: str
        :param column_range: str
        :return: dict
        """
        df = self.fetch_csv(sheet_url)
        if row_range is not None:
            tmp = row_range.split(':')
            s = int(tmp[0]) if len(tmp) > 1 and tmp[0] != '' else None
            e = int(tmp[1]) if len(tmp) > 1 and tmp[1] != '' else int(tmp[0])
            df = df.iloc[s:e]
        if column_range is not None:
            df = df[column_range.split(',')]

        return orjson.loads(df.to_json(orient='records'))

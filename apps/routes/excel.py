from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse

from apps.controllers import ExcelController

router = APIRouter()


@router.get("/v1/api/excel")
def fetch_excel(sheet_name: str, sheet_url: str, row_range: str = None, column_range: str = None):
    """Fetch csv data from url
        :param sheet_name: str
            example: Sheet1
        :param sheet_url: str
            example: https://example/data/full_data.xlsx
        :param row_range: str
            example:  - 1:2 mean (from row 1 until row before 2)
                      - :2 or 2 mean (get all data limit 2)
        :param column_range: str
            example:  - date,name,age mean (get all column only selected field)
        :return: dict
        """
    _data = ExcelController()
    _result = _data.fetch(sheet_name, sheet_url, row_range, column_range)
    return JSONResponse({'status': HTTPStatus.OK, 'data': _result}, status_code=HTTPStatus.OK)

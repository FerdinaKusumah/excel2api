import unittest

from starlette import applications
from starlette.testclient import TestClient

from app import app
from connection import Connection
# import setting
from setting import Setting

client = TestClient(app)


class TestExcelServiceApi(unittest.TestCase):

    def setUp(self):
        _setting = Setting()
        applications.conf = dict()
        conn = Connection()
        # get config
        applications.conf['config'] = _setting.load_config
        applications.conf['cache'] = conn.cache_conn()

    def test_positive(self):
        """Raw test positive test"""
        _url = 'http://localhost:8000/v1/api/excel?sheet_name=Sheet1&sheet_url=https://mdcune.psych.ucla.edu/modules/bioinformatics/extras/QTL_Sample_data.xls/at_download/file&column_range=ID,Point,Strain&row_range=3:5'
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_with_no_column_range(self):
        """Test with no column range"""
        _url = 'http://localhost:8000/v1/api/excel?sheet_name=Sheet1&sheet_url=https://mdcune.psych.ucla.edu/modules/bioinformatics/extras/QTL_Sample_data.xls/at_download/file&row_range=3:5'
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_with_no_row_range(self):
        """Test with no row range"""
        _url = 'http://localhost:8000/v1/api/excel?sheet_name=Sheet1&sheet_url=https://mdcune.psych.ucla.edu/modules/bioinformatics/extras/QTL_Sample_data.xls/at_download/file&column_range=ID,Point,Strain'
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_with_no_row_and_column_range(self):
        """Test with no column and row range"""
        _url = 'http://localhost:8000/v1/api/excel?sheet_name=Sheet1&sheet_url=https://mdcune.psych.ucla.edu/modules/bioinformatics/extras/QTL_Sample_data.xls/at_download/file'
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_with_no_sheet_url(self):
        """Test with no sheet url"""
        _url = 'http://localhost:8000/v1/api/excel?sheet_name=Sheet1'
        response = client.get(_url)
        self.assertEqual(response.status_code, 422)

    def test_with_no_sheet_name(self):
        """Test with no sheet name"""
        _url = 'http://localhost:8000/v1/api/excel?sheet_url=https://mdcune.psych.ucla.edu/modules/bioinformatics/extras/QTL_Sample_data.xls/at_download/file'
        response = client.get(_url)
        self.assertEqual(response.status_code, 422)

import unittest

from starlette import applications
from starlette.testclient import TestClient

from app import app
from connection import Connection
# import setting
from setting import Setting

client = TestClient(app)


class TestCsvServiceApi(unittest.TestCase):

    def setUp(self):
        _setting = Setting()
        applications.conf = dict()
        conn = Connection()
        # get config
        applications.conf['config'] = _setting.load_config
        applications.conf['cache'] = conn.cache_conn()

    def test_positive(self):
        """Raw test positive test"""
        _url = 'http://localhost:8000/v1/api/csv?sheet_url=https://covid.ourworldindata.org/data/ecdc/full_data.csv&column_range=date,location,new_cases&row_range=1:2'
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_with_no_column_range(self):
        """Test with no column range"""
        _url = 'http://localhost:8000/v1/api/csv?sheet_url=https://covid.ourworldindata.org/data/ecdc/full_data.csv&row_range=1:2'
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_with_no_row_range(self):
        """Test with no row range"""
        _url = 'http://localhost:8000/v1/api/csv?sheet_url=https://covid.ourworldindata.org/data/ecdc/full_data.csv&column_range=date,location,new_cases'
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_with_no_row_and_column_range(self):
        """Test with no column and row range"""
        _url = 'http://localhost:8000/v1/api/csv?sheet_url=https://covid.ourworldindata.org/data/ecdc/full_data.csv'
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_with_no_sheet_url(self):
        """Test with no sheet url"""
        _url = 'http://localhost:8000/v1/api/csv?column_range=date,location,new_cases&row_range=1:2'
        response = client.get(_url)
        self.assertEqual(response.status_code, 422)

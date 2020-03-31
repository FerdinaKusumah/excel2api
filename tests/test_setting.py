import unittest

from setting import Setting


class TestSetting(unittest.TestCase):

    def test_load_config(self):
        """Unit test function list"""
        _setting = Setting()
        _conf = _setting.load_config
        self.assertIsNotNone(_conf)

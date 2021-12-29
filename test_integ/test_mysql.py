import unittest
import config
from dao.mysql import DB


class TestMySQLdb(unittest.TestCase):
    def test_exec(self):
        db = DB(config.MySqlDb)
        ret = db.execute('select 1')
        expected = [(1,)]
        self.assertEqual(ret, expected)


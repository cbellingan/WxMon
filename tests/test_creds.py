import unittest
from utils import Creds

class TestCreds(unittest.TestCase):

    def test_read_creds(self):
        #TODO: don't love doing this with a python object as it becomes tempting to add logic to that class which
        # isn't what a config is for. TBD.
        c = Creds.get_creds('MySqlDb')
        self.assertEqual(c.username, 'username')
        self.assertEqual(c.password, 'password')
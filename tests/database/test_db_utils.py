

import unittest2

from thanatos.database import db_utils


class DatabaseUtilsTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    def test_db_connection_defaults(self):
        """ Test that the default connection details get set correctly when no env set. """

        db_connection_details = db_utils.get_default_connection_details()

        self.assertEqual(db_connection_details, {
            'host': '127.0.0.1',
            'user': 'vagrant',
            'password': 'vagrant',
            'database': 'thanatos',
        })

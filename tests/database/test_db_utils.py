

import mock
import unittest2

from thanatos.database import db_utils


class DatabaseUtilsTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    @mock.patch('os.environ')
    def test_db_connection_gets_c9_default(self, mock_environ):
        """ Test that the default connection details get set correctly when run on C9. """

        mock_environ.get.side_effect = [
            'thanatos',
            '0.0.0.0',
            'cloud 9',
        ]

        db_connection_details = db_utils.get_default_connection_details()

        self.assertEqual(db_connection_details, {
            'host': '0.0.0.0',
            'user': 'cloud 9',
            'password': '',
            'database': 'c9',
        })

    @mock.patch('os.environ')
    def test_db_connection_defaults(self, mock_environ):
        """ Test that the default connection details get set correctly when not run on C9. """

        mock_environ.get.return_value = None

        db_connection_details = db_utils.get_default_connection_details()

        self.assertEqual(db_connection_details, {
            'host': '127.0.0.1',
            'user': 'vagrant',
            'password': 'vagrant',
            'database': 'thanatos',
        })

    @mock.patch('urllib.urlretrieve')
    def test_download_tables(self, mock_urlretrieve):
        base_url    = 'http://example.com/'
        tables_list = [
            'table_one',
            'table_two',
        ]

        db_utils.download_tables(tables_list, base_url)

        mock_urlretrieve.assert_any_call('http://example.com/table_one.sql.bz2', 'table_one.sql.bz2')
        mock_urlretrieve.assert_any_call('http://example.com/table_two.sql.bz2', 'table_two.sql.bz2')
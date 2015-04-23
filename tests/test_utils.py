

import mock
import unittest2

from thanatos import utils


class UtilsTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    @mock.patch('urllib.urlretrieve')
    def test_download_tables(self, mock_urlretrieve):
        base_url    = 'http://example.com/'
        tables_list = [
            'table_one',
            'table_two',
        ]

        utils.download_tables(tables_list, base_url)

        mock_urlretrieve.assert_any_call('http://example.com/table_one.sql.bz2', 'table_one.sql.bz2')
        mock_urlretrieve.assert_any_call('http://example.com/table_two.sql.bz2', 'table_two.sql.bz2')

    def test_get_table_filename(self):
        table_name = 'test_one'
        table_file_name = utils.get_table_filename(table_name)

        self.assertEqual(table_file_name, 'test_one.sql.bz2')
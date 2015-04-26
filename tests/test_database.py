

import mock
import unittest2

from thanatos import database


class DatabaseTestCase(unittest2.TestCase):

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
        
        db_connection_details = database.get_default_connection_details()
        
        self.assertEqual(db_connection_details, {
            'host': '0.0.0.0',
            'user': 'cloud 9',
            'password': '',
            'database': 'c9',
        })

    @mock.patch('os.environ')
    def test_db_connection_defaults(self, mock_environ):
        """ Test that the default connection details get set correctly when run on C9. """
        
        mock_environ.get.return_value = None
        
        db_connection_details = database.get_default_connection_details()
        
        self.assertEqual(db_connection_details, {
            'host': '127.0.0.1',
            'user': 'vagrant',
            'password': 'vagrant',
            'database': 'thanatos',
        })

    def test_get_all_not_wh_regions_calls_execute(self):
        """ Test we can call get all not WH regions. """

        mock_db_connection = mock.MagicMock()

        database.get_all_not_wh_regions(mock_db_connection)

        mock_db_connection.cursor().execute.assert_was_called()

    def test_get_all_regions_connected_to_region_calls_execute(self):
        """ Test we can call the all regions connected to specified region. """

        mock_db_connection = mock.MagicMock()
        mock_region_id = 000

        database.get_all_regions_connected_to_region(mock_db_connection, mock_region_id)

        mock_db_connection.cursor().execute.assert_was_called()

    def test_get_all_published_ships_basic_calls_execute(self):
        """ Test we can call get all published ships basic. """

        mock_db_connection = mock.MagicMock()

        database.get_all_published_ships_basic(mock_db_connection)

        mock_db_connection.cursor().execute.assert_was_called()

    def test_get_dogma_attribute_for_type_calls_execute(self):
        """ Test we can call get spcified dogma attribute for specified type ID. """

        mock_db_connection = mock.MagicMock()
        mock_type_id = 000
        mock_dogma_attribute = 111

        database.get_dogma_attribute_for_type(mock_db_connection, mock_type_id, mock_dogma_attribute)

        mock_db_connection.cursor().execute.assert_was_called()
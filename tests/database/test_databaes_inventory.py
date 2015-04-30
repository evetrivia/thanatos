

import mock
import unittest2

from thanatos.database import inventory


class DatabaseInventoryTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    @mock.patch('thanatos.database.db_utils.execute_sql')
    def test_get_all_published_ships_basic_calls_execute(self, mock_db_utils):
        """ Test we can call get all published ships basic. """

        mock_db_connection = mock.MagicMock()

        inventory.get_all_published_ships_basic(mock_db_connection)

        mock_db_utils().assert_called_with()

    def test_get_dogma_attribute_for_type_calls_execute(self):
        """ Test we can call get spcified dogma attribute for specified type ID. """

        mock_db_connection = mock.MagicMock()
        mock_type_id = 000
        mock_dogma_attribute = 111

        inventory.get_dogma_attribute_for_type(mock_db_connection, mock_type_id, mock_dogma_attribute)

        mock_db_connection.cursor().execute.assert_was_called()
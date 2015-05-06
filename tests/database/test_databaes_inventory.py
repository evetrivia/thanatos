

import mock
import unittest2

from thanatos.database import inventory


class DatabaseInventoryTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    @mock.patch('thanatos.database.inventory.execute_sql')
    def test_get_all_published_ships_basic(self, mock_execute_sql):
        """ Test we can call get all published ships basic. """

        mock_db_connection = mock.MagicMock()
        mock_execute_sql.return_value = [(1, 'test')]

        results = inventory.get_all_published_ships_basic(mock_db_connection)

        mock_execute_sql.assert_called_with('CALL get_all_published_ships_basic();', mock_db_connection)
        self.assertEqual(results, [(1, 'test')])

    @mock.patch('thanatos.database.inventory.execute_sql')
    def test_get_dogma_attribute_for_type(self, mock_execute_sql):
        """ Test we can call get specified dogma attribute for specified type ID. """

        mock_db_connection = mock.MagicMock()
        mock_type_id = 0
        mock_dogma_attribute = 111
        mock_execute_sql.return_value = (1, 'test')

        results = inventory.get_dogma_attribute_for_type(mock_db_connection, mock_type_id, mock_dogma_attribute)

        mock_execute_sql.assert_called_with('CALL get_dogma_attribute_for_type(0, 111);', mock_db_connection, fetch='one')
        self.assertEqual(results, 1)

    @mock.patch('thanatos.database.inventory.execute_sql')
    def test_get_dogma_attribute_for_type_handles_none(self, mock_execute_sql):
        """ Test we can call get specified dogma attribute for specified type ID. """

        mock_db_connection = mock.MagicMock()
        mock_type_id = 0
        mock_dogma_attribute = 111
        mock_execute_sql.return_value = None

        results = inventory.get_dogma_attribute_for_type(mock_db_connection, mock_type_id, mock_dogma_attribute)

        mock_execute_sql.assert_called_with('CALL get_dogma_attribute_for_type(0, 111);', mock_db_connection, fetch='one')
        self.assertEqual(results, None)


import mock
import unittest2

from thanatos.database import universe


class DatabaseUniverseTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    @mock.patch('thanatos.database.universe.execute_sql')
    def test_get_all_regions(self, mock_execute_sql):
        """  """

        mock_db_connection = mock.MagicMock()
        mock_execute_sql.return_value = [(1, 'test')]

        results = universe.get_all_regions(mock_db_connection)

        mock_execute_sql.assert_called_with('CALL get_all_regions();', mock_db_connection)
        self.assertEqual(results, [(1, 'test')])

    @mock.patch('thanatos.database.universe.execute_sql')
    def test_get_all_not_wh_regions(self, mock_execute_sql):
        """  """

        mock_db_connection = mock.MagicMock()
        mock_execute_sql.return_value = [(1, 'test')]

        results = universe.get_all_not_wh_regions(mock_db_connection)

        mock_execute_sql.assert_called_with('CALL get_all_not_wh_regions();', mock_db_connection)
        self.assertEqual(results, [(1, 'test')])

    @mock.patch('thanatos.database.universe.execute_sql')
    def test_get_all_regions_connected_to_region(self, mock_execute_sql):
        """  """

        mock_db_connection = mock.MagicMock()
        mock_region_id = 101
        mock_execute_sql.return_value = [(1, 'test')]

        results = universe.get_all_regions_connected_to_region(mock_db_connection, mock_region_id)

        mock_execute_sql.assert_called_with('CALL get_all_regions_connected_to_region(101);', mock_db_connection)
        self.assertEqual(results, [(1, 'test')])
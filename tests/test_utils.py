

import mock
import unittest2

from thanatos import utils


class UtilsTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    @mock.patch('thanatos.questions.base.Question.__subclasses__')
    def test_required_tables_returns_unique_set(self, mock_subclasses):
        """  """
        mock_subclass_1 = mock.Mock()
        mock_subclass_1.required_tables = ['test']

        mock_subclass_2 = mock.Mock()
        mock_subclass_2.required_tables = ['test', 'other_test']

        mock_subclasses.return_value = [mock_subclass_1, mock_subclass_2]

        required_tables = utils.get_list_of_required_tables()

        self.assertEqual(
            required_tables,
            {'test', 'other_test'}
        )
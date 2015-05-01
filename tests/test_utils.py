

import mock
import unittest2

from thanatos import utils


class ThanatosUtilsTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    @mock.patch('thanatos.questions.base.Question')
    def test_get_all_categories(self, mock_question):
        """  """
        pass

        # mock_subclass_one = mock.MagicMock()
        # mock_subclass_two = mock.MagicMock()
        # mock_subclasses = [
        #     mock_subclass_one,
        #     mock_subclass_two,
        # ]
        #
        # mock_question.__subclasses__.return_value = mock_subclasses
        #
        # results = utils.get_all_categories()
        #
        # mock_question.assert_was_called()
        # self.assertEqual(results, [])


import mock
import unittest2

from thanatos.database  import DB
from thanatos.questions import inventory


class HighSlotsQuestionTestCase(unittest2.TestCase):

    def setUp(self):
        self.mock_db = mock.Mock(spec=DB)

    def test_class_initializes(self):
        """ Simply test we can create an instance of the class. """

        inventory.HighSlotsQuestion(self.mock_db)

    @mock.patch('thanatos.questions.base.Question.format_question')
    def test_question_ask(self, mock_format_question):
        self.mock_db.get_all_published_ships_basic.return_value = [(582L, 'Bantam', 25L, 'Frigate', 6L, 'Ship')]
        self.mock_db.get_dogma_attribute_for_type.return_value = 3

        inventory.HighSlotsQuestion(self.mock_db).ask()

        mock_format_question.assert_called_with(
            (3, 3),
            [(0, 0), (1, 1), (2, 2), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],
            'How many high slots does the Bantam have?',
        )
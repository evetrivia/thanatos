

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

    def test_high_slots_returns_proper_question(self):
        self.mock_db.get_all_published_ships_basic.return_value = []

        hsq = inventory.HighSlotsQuestion(self.mock_db)
        question = hsq.ask()

        self.assertEqual(question, None)
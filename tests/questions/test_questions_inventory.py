

import mock
import MySQLdb
import unittest2

from thanatos.questions import inventory


class SlotsQuestionTestCase(unittest2.TestCase):

    def setUp(self):
        self.mock_db_connection = mock.Mock(spec=MySQLdb.connection)

    def test_class_initializes(self):
        """ Simply test we can create an instance of the class. """

        inventory.SlotsQuestion(self.mock_db_connection)

    @mock.patch('thanatos.questions.inventory.inventory')
    @mock.patch('thanatos.questions.base.Question.format_question')
    @mock.patch('random.choice')
    def test_question_ask(self, mock_random_choice, mock_format_question, mock_db_inventory):
        """ Test we can call the slots question ask method. """

        mock_db_inventory.get_all_published_ships_basic.return_value = [(582L, 'Bantam', 25L, 'Frigate', 6L, 'Ship')]
        mock_db_inventory.get_dogma_attribute_for_type.side_effect = [
            None,
            3,
        ]

        mock_random_choice.side_effect = [
            'high',
            (582L, 'Bantam', 25L, 'Frigate', 6L, 'Ship'),
            (582L, 'Bantam', 25L, 'Frigate', 6L, 'Ship'),
        ]

        inventory.SlotsQuestion(self.mock_db_connection).ask()

        mock_format_question.assert_called_with(
            (3, 3),
            [(0, 0), (1, 1), (2, 2), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],
            'How many high slots does the Bantam have?',
        )


class ShipIDQuestionTestCase(unittest2.TestCase):

    def setUp(self):
        self.mock_db_connection = mock.Mock(spec=MySQLdb.connection)

    def test_class_initializes(self):
        """ Simply test we can create an instance of the class. """

        inventory.ShipImageIdentificationQuestion(self.mock_db_connection)

    @mock.patch('thanatos.questions.inventory.inventory')
    @mock.patch('thanatos.questions.base.Question.format_question')
    @mock.patch('random.choice')
    def test_question_ask(self, mock_random_choice, mock_format_question, mock_db_inventory):
        """ Test we can call the ship identification question ask method. """

        mock_db_inventory.get_all_published_ships_basic.return_value = [
            (582L, 'Bantam', 25L, 'Frigate', 6L, 'Ship'),
            (583L, 'Tristin', 25L, 'Frigate', 6L, 'Ship'),
            (584L, 'Atron', 25L, 'Frigate', 6L, 'Ship'),
        ]

        mock_random_choice.return_value = (582L, 'Bantam', 25L, 'Frigate', 6L, 'Ship')

        inventory.ShipImageIdentificationQuestion(self.mock_db_connection).ask()

        mock_format_question.assert_called_with(
            (582L, 'Bantam', 25L, 'Frigate', 6L, 'Ship'),
            [(583L, 'Tristin'), (584L, 'Atron')],
            'What ship is pictured?',
            add_images_to_question=True
        )
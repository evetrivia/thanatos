

import mock
import MySQLdb
import unittest2

from thanatos.questions.base import Question


class QuestionsBaseTestCase(unittest2.TestCase):

    def setUp(self):
        self.mock_db_connection = mock.Mock(spec=MySQLdb.connection)

    def test_class_initializes(self):
        """ Simply test we can create an instance of the Test Question class. """

        TestableBaseQuestion(self.mock_db_connection)
    
    def test_basic_ask(self):
        """ If this somehow breaks... something great has gone wrong. This test
        simple exists to help bump the test coverage number up. The ask method
        shouldn't actually do anything."""

        TestableBaseQuestion(self.mock_db_connection).ask()

    @mock.patch('thanatos.questions.base.Question')
    @mock.patch('random.sample')
    @mock.patch('random.shuffle')
    def test_format_question(self, mock_shuffle, mock_sample, mock_question):
        """ Test that the format_question method returns the correct data. """

        question = 'What region is the best test region?'
        correct_answer = (10000001L, 'Derelik')
        possible_wrong_answers = [
            (10000004L, 'UUA-F4'),
            (10000017L, 'J7HZ-F'),
        ]

        mock_sample.return_value = possible_wrong_answers

        test_question = TestableBaseQuestion(self.mock_db_connection)
        question = test_question.format_question(correct_answer, possible_wrong_answers, question)

        mock_shuffle.assert_called_with([
            (10000004L, 'UUA-F4'),
            (10000017L, 'J7HZ-F'),
            (10000001L, 'Derelik'),
        ])

        mock_question.convert_choices_to_dict.assert_was_called()
        mock_question.convert_choices_to_dict.return_value = [
            {'text': 'UUA-F4',  'value': 10000004L},
            {'text': 'J7HZ-F',  'value': 10000017L},
            {'text': 'Derelik', 'value': 10000001L},
        ]

        self.assertEqual(question, {
            'answer'   : 10000001L,
            'question' : 'What region is the best test region?',
            'choices'  : [
                {'text': 'UUA-F4',  'value': 10000004L},
                {'text': 'J7HZ-F',  'value': 10000017L},
                {'text': 'Derelik', 'value': 10000001L},
            ],
        })

    @mock.patch('thanatos.questions.base.Question')
    @mock.patch('random.sample')
    @mock.patch('random.shuffle')
    def test_format_question_with_image(self, mock_shuffle, mock_sample, mock_question):
        """ Test that the format_question method returns the correct data specifically also with the image link. """

        question = 'What region is the best test region?'
        correct_answer = (10000001L, 'Derelik')
        possible_wrong_answers = [
            (10000004L, 'UUA-F4'),
            (10000017L, 'J7HZ-F'),
        ]

        mock_sample.return_value = possible_wrong_answers

        test_question = TestableBaseQuestion(self.mock_db_connection)
        question = test_question.format_question(correct_answer, possible_wrong_answers, question, add_images_to_question=True)

        mock_shuffle.assert_called_with([
            (10000004L, 'UUA-F4'),
            (10000017L, 'J7HZ-F'),
            (10000001L, 'Derelik'),
        ])

        mock_question.convert_choices_to_dict.assert_was_called()
        mock_question.convert_choices_to_dict.return_value = [
            {'text': 'UUA-F4',  'value': 10000004L},
            {'text': 'J7HZ-F',  'value': 10000017L},
            {'text': 'Derelik', 'value': 10000001L},
        ]

        self.assertEqual(question, {
            'answer'   : 10000001L,
            'question' : 'What region is the best test region?',
            'choices'  : [
                {'text': 'UUA-F4',  'value': 10000004L},
                {'text': 'J7HZ-F',  'value': 10000017L},
                {'text': 'Derelik', 'value': 10000001L},
            ],
            'images': {
                32: 'https://image.eveonline.com/Render/10000001_32.png',
                64: 'https://image.eveonline.com/Render/10000001_64.png',
                128: 'https://image.eveonline.com/Render/10000001_128.png',
                256: 'https://image.eveonline.com/Render/10000001_256.png',
                512: 'https://image.eveonline.com/Render/10000001_512.png',
            },
        })

    def test_convert_choices_to_dict(self):
        """ Test that convert_choices_to_dict properly converts. """

        choices = [
            (10000004L, 'UUA-F4'),
            (10000017L, 'J7HZ-F'),
            (10000001L, 'Derelik'),
        ]

        test_question     = TestableBaseQuestion(self.mock_db_connection)
        converted_choices = test_question.convert_choices_to_dict(choices)

        self.assertEqual(converted_choices, [
            {'text': 'UUA-F4',  'value': 10000004L},
            {'text': 'J7HZ-F',  'value': 10000017L},
            {'text': 'Derelik', 'value': 10000001L},
        ])


class TestableBaseQuestion(Question):
    """ A subclass of the base class to test against. """

    def ask(self):
        pass
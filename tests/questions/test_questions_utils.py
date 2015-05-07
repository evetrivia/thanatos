

import mock
import unittest2

from thanatos.questions import question_utils


class QuestionsUtilsTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    @mock.patch('thanatos.questions.question_utils.get_question_subclasses')
    @mock.patch('thanatos.questions.question_utils.choice')
    def test_get_random_question(self, mock_choice, mock_get_question_subclasses):
        """ Test to make sure the number in a list is multiplied by it's weight. """

        mock_question = mock.MagicMock()
        mock_question.random_weight = 3
        mock_get_question_subclasses.return_value = [mock_question]

        question_utils.get_random_question()

        mock_choice.assert_called_with([
            mock_question,
            mock_question,
            mock_question,
        ])

    def test_get_question(self):
        """ Test the get question method works. """

        question_utils.get_question('slotsquestion')

    def test_get_question_bad_question(self):
        """ Test the get question method returns a proper exception if an invalid question is specified. """

        self.failUnlessRaises(
            question_utils.InvalidQuestionException,
            question_utils.get_question,
            'invalidquestion',
        )

    def test_get_question_from_category(self):
        """ Test the get_question_from_category method works. """

        question_utils.get_question_from_category('inventory')

    def test_get_question_from_category_bad_category(self):
        """ Test the get_question_from_category method raises proper exception. """

        self.failUnlessRaises(
            question_utils.InvalidQuestionCategoryException,
            question_utils.get_question_from_category,
            'invalidcategory',
        )

    def test_get_question_from_sub_category(self):
        """ Test the get_question_from_sub_category method works. """

        question_utils.get_question_from_sub_category('inventory', 'slots')

    def test_get_question_from_sub_category_bad_category(self):
        """ Test the get_question_from_subcategory method raises the proper exception. """

        self.failUnlessRaises(
            question_utils.InvalidQuestionCategoryException,
            question_utils.get_question_from_sub_category,
            'invalidcategory',
            'invalidsubcategory',
        )

    def test_get_all_question_details(self):
        """ Test the get_all_question_details method works. """

        question_utils.get_all_question_details()
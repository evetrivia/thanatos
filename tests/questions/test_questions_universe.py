

import mock
import MySQLdb
import unittest2

from thanatos.questions import universe


class BorderingRegionsTestCase(unittest2.TestCase):

    def setUp(self):
        self.mock_db_connection = mock.Mock(spec=MySQLdb.connection)

    def test_class_initializes(self):
        """ Simply test we can create an instance of the BRQ class. """

        universe.BorderingRegionsQuestion(self.mock_db_connection)

    @mock.patch('thanatos.questions.universe.universe')
    @mock.patch('thanatos.questions.base.Question.format_question')
    @mock.patch('random.choice')
    def test_question_ask(self, random_choice, mock_format_question, mock_db_universe):
        """ Test we can call the bordering region question ask method. """

        all_regions = [
            (10000001L, 'Region One'),
            (10000002L, 'Region Two'),
            (10000003L, 'Region Three'),
            (10000004L, 'Region Four'),
            (10000005L, 'Region Five'),
            (10000006L, 'Region Six'),
        ]

        mock_db_universe.get_all_not_wh_regions.return_value = all_regions

        random_choice.side_effect = [
            (10000001L, 'Region One'),
            (10000005L, 'Region Five'),
        ]

        mock_db_universe.get_all_regions_connected_to_region.return_value = [
            (10000005L, 'Region Five'),
            (10000006L, 'Region Six'),
        ]

        universe.BorderingRegionsQuestion(self.mock_db_connection).ask()

        random_choice.assert_any_call(all_regions)
        random_choice.assert_any_call([
            (10000005L, 'Region Five'),
            (10000006L, 'Region Six'),
        ])

        mock_format_question.assert_called_with(
            (10000005L, 'Region Five'),
            [(10000003L, 'Region Three'), (10000002L, 'Region Two'), (10000004L, 'Region Four')],
            'Which of the following regions borders the Region One region?',
        )


class PoitotTestCase(unittest2.TestCase):

    def setUp(self):
        self.mock_db_connection = mock.Mock(spec=MySQLdb.connection)

    def test_class_initializes(self):
        """ Simply test we can create an instance of the Poitot questions class. """

        universe.PoitotFamousForQuestion(self.mock_db_connection)

    @mock.patch('thanatos.questions.base.Question.format_question')
    def test_question_ask(self, mock_format_question):
        """ Test we can call the poitot question ask method. """

        universe.PoitotFamousForQuestion(self.mock_db_connection).ask()

        mock_format_question.assert_called_with(
            (0, 'The only named system in Syndicate.'),
            [(1, 'Kind to animals.'), (2, 'A fictional space detective.'), (3, 'Adjacent to F67E-Q.')],
            'Poitot is famous for being...?',
        )


class UniverseUtilsTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    def test_removal_of_regions(self):
        """ Specifically tests to make sure we remove the jove regions with no gates. """

        sample_regions_list = [
            (10000001L, 'Derelik'),
            (10000004L, 'UUA-F4'),
            (10000017L, 'J7HZ-F'),
            (10000019L, 'A821-A'),
        ]

        gateless_regions = universe.remove_regions_with_no_gates(sample_regions_list)

        self.assertEqual(gateless_regions, [(10000001L, 'Derelik')])

    def test_removal_of_regions_handles_region_not_in_list(self):
        """ Specifically tests we don't fail removing a region if it doesn't exist in the list. """

        sample_regions_list = [
            (10000001L, 'Derelik'),
            (10000004L, 'UUA-F4'),
        ]

        gateless_regions = universe.remove_regions_with_no_gates(sample_regions_list)

        self.assertEqual(gateless_regions, [(10000001L, 'Derelik')])


import mock
import unittest2

from thanatos.database  import DB
from thanatos.questions import universe


class BorderingRegionsTestCase(unittest2.TestCase):

    def setUp(self):
        self.mock_db = mock.Mock(spec=DB)

    def test_class_initializes(self):
        """ Simply test we can create an instance of the BRQ class. """

        universe.BorderingRegionsQuestion(self.mock_db)

    # def test_question_ask(self):
    #
    #     self.mock_db.get_all_not_wh_regions.return_value = [
    #         (10000001L, 'Derelik'),
    #     ]
    #
    #     self.mock_db.get_all_regions_connected_to_region.return_value = [
    #
    #     ]
    #
    #     brq = universe.BorderingRegionsQuestion(self.mock_db)
    #     brq.ask()

class PoitotTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    def test_class_initializes(self):
        """ Simply test we can create an instance of the Poitot questions class. """

        universe.PoitotFamousForQuestion()


class UniverseUtilsTestCase(unittest2.TestCase):

    def setUp(self):
        self.mock_db = mock.Mock(spec=DB)

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
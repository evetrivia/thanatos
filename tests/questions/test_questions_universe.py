

import unittest2

from thanatos.questions import universe


class BorderingRegionsTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    def test_class_initializes(self):
        """ Simply test we can create an instance of the BRQ class. """

        universe.BorderingRegionsQuestion()


class PoitotTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    def test_class_initializes(self):
        """ Simply test we can create an instance of the Poitot questions class. """

        universe.PoitotFamousForQuestion()
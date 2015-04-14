

import mock
import unittest2

from thanatos import database


class DatabaseTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    def test_class_initializes(self):
        """ Simply test we can create an instance of the DB class. """

        database.DB()
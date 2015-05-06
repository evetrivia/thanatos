

import mock
import unittest2

from thanatos.questions import question_utils


class ThanatosUtilsTestCase(unittest2.TestCase):

    def setUp(self):
        pass
    
    def test_get_question_subclasses(self):
        question_utils.get_question_subclasses()
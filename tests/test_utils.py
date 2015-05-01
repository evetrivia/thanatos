

import mock
import unittest2

from thanatos import utils


class ThanatosUtilsTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    @mock.patch('thanatos.utils.get_question_subclasses')
    def test_get_all_categories(self, mock_question):
        """  """
        pass

        mock_subclass_one = mock.MagicMock()
        mock_subclass_one.category_primary = 'Universe'
        mock_subclass_one.category_secondary = 'Regions'
        mock_subclass_one.random_weight = 1
        mock_subclass_one.__name__ = 'Subclass One'
        
        mock_subclass_two = mock.MagicMock()
        mock_subclass_two.category_primary = 'Inventory'
        mock_subclass_two.category_secondary = 'Slots'
        mock_subclass_two.random_weight = 2
        mock_subclass_two.__name__ = 'Subclass Two'
        
        mock_subclass_three = mock.MagicMock()
        mock_subclass_three.category_primary = 'Inventory'
        mock_subclass_three.category_secondary = 'Identification'
        mock_subclass_three.random_weight = 3
        mock_subclass_three.__name__ = 'Subclass Three'
        
        mock_subclass_four = mock.MagicMock()
        mock_subclass_four.category_primary = 'Inventory'
        mock_subclass_four.category_secondary = 'Identification'
        mock_subclass_four.random_weight = 4
        mock_subclass_four.__name__ = 'Subclass Four'
        
        mock_subclass_five = mock.MagicMock()
        mock_subclass_five.category_primary = None
        mock_subclass_five.category_secondary = None
        
        mock_subclasses = [
            mock_subclass_one,
            mock_subclass_two,
            mock_subclass_three,
            mock_subclass_four,
            mock_subclass_five,
        ]
        
        mock_question.return_value = mock_subclasses
        
        results = utils.get_all_categories()
        
        mock_question.assert_was_called()
        self.assertEqual(results, {
            'Universe': {
                'Regions': {
                    'Subclass One': 1,
                },
            },
            'Inventory': {
                'Slots': {
                    'Subclass Two': 2,
                },
                'Identification': {
                    'Subclass Three': 3,
                    'Subclass Four': 4,
                },
            },
        })
    
    def test_get_question_subclasses(self):
        utils.get_question_subclasses()
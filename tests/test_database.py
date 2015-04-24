

import mock
import unittest2

from thanatos import database


class DatabaseTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    def test_class_initializes(self):
        """ Simply test we can create an instance of the DB class. """

        database.DB()
    
    @mock.patch('os.environ')
    def test_db_connection_gets_c9_default(self, mock_environ):
        """ Test that the default connection details get set correctly when run on C9. """
        
        mock_environ.get.side_effect = [
            'thanatos',
            '0.0.0.0',
            'cloud 9',
        ]
        
        db = database.DB()
        
        self.assertEqual('0.0.0.0', db.host)
        self.assertEqual('cloud 9', db.user)
        self.assertEqual('', db.password)
        self.assertEqual('c9', db.database)

    @mock.patch('os.environ')
    def test_db_connection_defaults(self, mock_environ):
        """ Test that the default connection details get set correctly when run on C9. """
        
        mock_environ.get.return_value = None
        
        db = database.DB()
        
        self.assertEqual('127.0.0.1', db.host)
        self.assertEqual('vagrant', db.user)
        self.assertEqual('vagrant', db.password)
        self.assertEqual('thanatos', db.database)
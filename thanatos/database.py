

import os
import MySQLdb


def load_table(table_name):
    """ Given a table name it loads the file from disk and executes on the DB.
    
    :param table_name:
    :type table_name:
    
    """
    

class DB(object):
    def __init__(self, connection_string=None):
        self.conn = None
        self.connection_string = connection_string

        if self.connection_string is None:
            self.connection_string = self._get_default_connection_string()

    def connect(self):
        self.conn = MySQLdb.connect(self.host, self.user, self.password, self.sqldb)

    @staticmethod
    def _get_default_connection_string():
        return ''
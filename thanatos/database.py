

import os
import MySQLdb


def load_table(table_name):
    """ Given a table name it loads the file from disk and executes on the DB.
    
    :param table_name:
    :type table_name:
    
    """
    
    
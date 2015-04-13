

import os
import MySQLdb
import logging

_log = logging.getLogger('thanatos.database')
    

class DB(object):
    def __init__(self, host=None, user=None, password=None, database=None):
        self._connection = None

        self.host     = host
        self.user     = user
        self.password = password
        self.database = database

        if None in (self.host, self.user, self.password, self.database):
            self._set_default_connection_details()

    @property
    def connection(self):
        """ Checks if the connection object exists yet, if not creates it and returns it.

        :return: A MySQLdb connection
        :rtype: MySQLdb.connections.Connection
        """

        if self._connection is None:
            self._connect()

        return self._connection

    def _connect(self):
        """ Creates a connection to the MySQL DB. """

        self._connection = MySQLdb.connect(self.host, self.user, self.password, self.database)

    def _set_default_connection_details(self):
        """ Sets the connection details based on environment vars or Thanatos default settings. """

        if os.environ.get('C9_PROJECT') is not None:
            pass

        else:
            self.host     = '127.0.0.1'
            self.user     = 'vagrant'
            self.password = 'vagrant'
            self.database = 'thanatos'
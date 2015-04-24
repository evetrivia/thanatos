

import os
import MySQLdb
import logging

_log = logging.getLogger('thanatos.database')
    

class DB(object):
    required_tables = [
        'dgmTypeAttributes',
        'invTypes',
        'invGroups',
        'invCategories',
        'mapRegions',
        'mapRegionJumps',
    ]

    def __init__(self, host=None, user=None, password=None, database=None):
        self._connection = None

        self.host     = host
        self.user     = user
        self.password = password
        self.database = database

        if None in (self.host, self.user, self.password, self.database):
            _log.info('One of host, user, password, or database was not set')
            self._set_default_connection_details()

    def execute(self, sql):
        """
        :param sql: SQL statement to be executed
        :type sql: str

        :return: Lit of results
        :rtype: list
        """

        cursor = self.connection.cursor()

        cursor.execute(sql)

        return [x for x in cursor.fetchall()]

    @property
    def connection(self):
        """ Checks if the connection object exists yet, if not creates it and returns it.

        :return: A MySQLdb connection
        :rtype: MySQLdb.connections.Connection
        """

        if self._connection is None:
            self._connect()

        return self._connection

    def get_all_not_wh_regions(self):
        """ Gets a list of all regions that are not WH regions.

        :return: A list of all regions not including wormhole regions. Results have regionID and regionName.
        :rtype: list
        """

        sql = '''
            SELECT mapRegions.regionID, mapRegions.regionName
              FROM mapRegions
             WHERE mapRegions.regionID < 11000000
        '''

        return self.execute(sql)

    def get_all_regions_connected_to_region(self, region_id):
        """ Gets a list of all regions connected to the region ID passed in.

        :param region_id: Region ID to find all regions connected to.
        :type region_id: int

        :return: A list of all regions connected to the specified region ID. Results have regionID and regionName.
        :rtype: list
        """

        sql = '''
            SELECT mapRegionJumps.toRegionID AS regionID, mapRegions.regionName
              FROM mapRegionJumps
              LEFT JOIN mapRegions ON mapRegions.regionID = mapRegionJumps.toRegionID
             WHERE mapRegionJumps.fromRegionID = {}
        '''.format(region_id)

        return self.execute(sql)

    def get_all_published_ships_basic(self):
        """ Gets a list of all published ships and their basic information.

        :return: Each result has a tuple of (typeID, typeName, groupID, groupName, categoryID, and categoryName).
        :rtype: list
        """

        sql = '''
            SELECT invTypes.typeID, invTypes.typeName,
                   invGroups.groupID, invGroups.groupName,
                   invCategories.categoryID, invCategories.categoryName
              FROM invTypes
             INNER JOIN invGroups ON invTypes.groupID = invGroups.groupID
             INNER JOIN invCategories ON invGroups.categoryID = invCategories.categoryID
             WHERE invCategories.categoryID = 6
               AND invTypes.published = 1
        '''

        return self.execute(sql)

    def get_dogma_attribute_for_type(self, type_id, dogma_attribute):
        """

        :param type_id:
        :param dogma_attribute:

        :return:
        :rtype:
        """

        sql = '''
            SELECT COALESCE(dgmTypeAttributes.valueInt, dgmTypeAttributes.valueFloat)
              FROM invTypes
              LEFT JOIN dgmTypeAttributes ON invTypes.typeID = dgmTypeAttributes.typeID
             WHERE invTypes.typeID = {}
               AND dgmTypeAttributes.attributeID = {}
        '''.format(type_id, dogma_attribute)

        result = self.execute(sql)

        return result[0][0]  # self.execute always returns a list of tuples

    def _connect(self):
        """ Creates a connection to the MySQL DB. """

        self._connection = MySQLdb.connect(self.host, self.user, self.password, self.database)

    def _set_default_connection_details(self):
        """ Sets the connection details based on environment vars or Thanatos default settings. """

        _log.info('Setting default datbase connetion details.')

        if os.environ.get('C9_PROJECT') is not None:
            _log.info('C9_PROJECT environment found. Setting C9 DB connection details.')
            
            # See https://docs.c9.io/v1.0/docs/setting-up-mysql
            self.host = os.environ.get('IP')
            self.user = os.environ.get('C9_USER')
            self.password = ''
            self.database = 'c9'

        else:
            _log.info('Using Vagrant DB default connection details.')
            
            self.host = '127.0.0.1'
            self.user = 'vagrant'
            self.password = 'vagrant'
            self.database = 'thanatos'
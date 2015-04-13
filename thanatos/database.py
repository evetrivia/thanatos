

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

    def execute(self, sql):
        """
        :param sql: SQL statement to be executed
        :type sql: str

        :return: Lit of results
        :rtype: list
        """

        cursor = self.connection.cursor()

        cursor.execute(sql)

        return cursor.fetchall()

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

        :return: Each result has typeID, typeName, groupID, groupName, categoryID, and categoryName.
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
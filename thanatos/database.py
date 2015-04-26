

import os
import MySQLdb
import logging

_log = logging.getLogger('thanatos.database')

required_tables = [
    'dgmTypeAttributes',
    'invTypes',
    'invGroups',
    'invCategories',
    'mapRegions',
    'mapRegionJumps',
]


def get_all_not_wh_regions(db_connection):
    """ Gets a list of all regions that are not WH regions.

    :return: A list of all regions not including wormhole regions. Results have regionID and regionName.
    :rtype: list
    """

    sql = '''
        SELECT mapRegions.regionID, mapRegions.regionName
          FROM mapRegions
         WHERE mapRegions.regionID < 11000000
    '''
    
    cursor = db_connection.cursor()
    cursor.execute(sql)

    return cursor.fetchall()


def get_all_regions_connected_to_region(db_connection, region_id):
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

    cursor = db_connection.cursor()
    cursor.execute(sql)

    return cursor.fetchall()


def get_all_published_ships_basic(db_connection):
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

    cursor = db_connection.cursor()
    cursor.execute(sql)

    return cursor.fetchall()


def get_dogma_attribute_for_type(db_connection, type_id, dogma_attribute):
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

    cursor = db_connection.cursor()
    cursor.execute(sql)

    return cursor.fetchone()[0]


def get_connection(connection_details=None):
    """ Creates a connection to the MySQL DB. """
    
    if connection_details is None:
        connection_details = get_default_connection_details()

    return MySQLdb.connect(
        connection_details['host'],
        connection_details['user'],
        connection_details['password'],
        connection_details['database']
    )


def get_default_connection_details():
    """ Gets the connection details based on environment vars or Thanatos default settings.
    
    :return: Returns a dictionary of connection details.
    :rtype: dict
    """

    _log.info('Getting default database connetion details.')

    if os.environ.get('C9_PROJECT') is not None:
        _log.info('C9_PROJECT environment found. Getting C9 DB connection details.')
        
        # See https://docs.c9.io/v1.0/docs/setting-up-mysql
        
        return {
            'host': os.environ.get('IP'),
            'user': os.environ.get('C9_USER'),
            'password': '',
            'database': 'c9',
        }

    else:
        _log.info('Getting Vagrant DB default connection details.')
        
        return {
            'host': '127.0.0.1',
            'user': 'vagrant',
            'password': 'vagrant',
            'database': 'thanatos',
        }
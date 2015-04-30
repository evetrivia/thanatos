

import logging

from thanatos.database.db_utils import execute_sql

_log = logging.getLogger('thanatos.database.universe')


def get_all_regions(db_connection):
    """ Gets a list of all regions.

    :return: A list of all regions. Results have regionID and regionName.
    :rtype: list
    """

    sql = 'CALL get_all_regions();'
    results = execute_sql(sql, db_connection)

    return results


def get_all_not_wh_regions(db_connection):
    """ Gets a list of all regions that are not WH regions.

    :return: A list of all regions not including wormhole regions. Results have regionID and regionName.
    :rtype: list
    """

    sql = 'CALL get_all_not_wh_regions();'
    results = execute_sql(sql, db_connection)

    return results


def get_all_regions_connected_to_region(db_connection, region_id):
    """ Gets a list of all regions connected to the region ID passed in.

    :param region_id: Region ID to find all regions connected to.
    :type region_id: int

    :return: A list of all regions connected to the specified region ID. Results have regionID and regionName.
    :rtype: list
    """

    sql = 'CALL get_all_regions_connected_to_region({});'.format(region_id)
    results = execute_sql(sql, db_connection)

    return results
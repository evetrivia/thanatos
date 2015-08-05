

import logging

from thanatos.database.db_utils import execute_sql

_log = logging.getLogger('thanatos')


def get_all_published_ships_basic(db_connection):
    """ Gets a list of all published ships and their basic information.

    :return: Each result has a tuple of (typeID, typeName, groupID, groupName, categoryID, and categoryName).
    :rtype: list
    """

    if not hasattr(get_all_published_ships_basic, '_results'):
        sql = 'CALL get_all_published_ships_basic();'
        results = execute_sql(sql, db_connection)
        get_all_published_ships_basic._results = results

    return get_all_published_ships_basic._results


def get_dogma_attribute_for_type(db_connection, type_id, dogma_attribute):
    """

    :param type_id:
    :param dogma_attribute:

    :return:
    :rtype:
    """

    sql = 'CALL get_dogma_attribute_for_type({}, {});'.format(type_id, dogma_attribute)
    results = execute_sql(sql, db_connection, fetch='one')

    if results is not None:
        results = results[0]  # It's returned as a tuple from the DB, lets change that.

    return results


def get_ships_that_have_variations(db_connection):
    """ Gets a list of all published ship type IDs that have at least 3 variations.

    :return:
    :rtype: list
    """

    if not hasattr(get_ships_that_have_variations, '_results'):
        sql = 'CALL get_ships_that_have_variations();'
        results = execute_sql(sql, db_connection)
        get_ships_that_have_variations._results = results

    return get_ships_that_have_variations._results


def get_type_variations(db_connection, type_id):
    """

    :param type_id:
    :param dogma_attribute:

    :return:
    :rtype:
    """

    sql = 'CALL get_variations_for_type_id({});'.format(type_id)
    results = execute_sql(sql, db_connection)

    return results

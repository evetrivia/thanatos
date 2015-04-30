

import logging

from thanatos.database.db_utils import execute_sql

_log = logging.getLogger('thanatos.database.inventory')


def get_all_published_ships_basic(db_connection):
    """ Gets a list of all published ships and their basic information.

    :return: Each result has a tuple of (typeID, typeName, groupID, groupName, categoryID, and categoryName).
    :rtype: list
    """

    sql = 'CALL get_all_published_ships_basic();'
    results = execute_sql(sql, db_connection)

    return results


def get_dogma_attribute_for_type(db_connection, type_id, dogma_attribute):
    """

    :param type_id:
    :param dogma_attribute:

    :return:
    :rtype:
    """

    sql = 'CALL get_dogma_attribute_for_type({}, {});'.format(type_id, dogma_attribute)
    results = execute_sql(sql, db_connection, fetch_one=True)

    return results
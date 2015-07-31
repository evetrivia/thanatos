

import os
import MySQLdb
import logging

_log = logging.getLogger('thanatos')


def execute_sql(sql, db_connection, fetch='all'):
    """

    :param sql:
    :param db_connection:
    :param fetch: A string of either 'all' or 'one'.

    :return:
    """

    cursor = db_connection.cursor()
    cursor.execute(sql)

    if fetch == 'all':
        results = [x for x in cursor.fetchall()]

    elif fetch == 'one':
        results = cursor.fetchone()

    else:
        results = None

    cursor.close()

    return results


def get_stored_procs(db_connection):
    """
    :param db_connection:
    :return:
    """

    sql = "SHOW PROCEDURE STATUS;"
    procs = execute_sql(sql, db_connection)

    return [x[1] for x in procs]

def drop_proc(proc_name, db_connection):
    """

    :param proc_name:
    :param db_connection:
    :return:
    """

    sql = "DROP PROCEDURE {};".format(proc_name)
    execute_sql(sql, db_connection)

def update_sql_stored_procs(db_connection):
    """

    :param db_connection:

    :return:
    """

    procs_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'procs')
    existing_procs = get_stored_procs(db_connection)

    for proc_file_name in os.listdir(procs_dir_path):
        _log.info('Running {}'.format(proc_file_name))

        proc_file_path = os.path.join(procs_dir_path, proc_file_name)
        proc_name = proc_file_name.split('.')[1]

        if proc_name in existing_procs:
            drop_proc(proc_name, db_connection)

        with open(proc_file_path, 'r') as sql_file:
            sql = " ".join(sql_file.readlines())
            execute_sql(sql, db_connection, fetch=None)


def load_tables_from_files(db_connection):
    """ Looks in the current working directory for all required tables. """

    _log.info('Loading tables from disk to DB.')

    sde_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sde')

    for sde_file_name in os.listdir(sde_dir_path):
        _log.info('Loading the following table: {}'.format(sde_file_name))

        sde_file_path = os.path.join(sde_dir_path, sde_file_name)

        with open(sde_file_path, 'r') as sde_file:
            sql = sde_file.read()
            execute_sql(sql, db_connection)

    _log.info('Finished loading all requested tables.')


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

    return {
        'host': os.environ.get('MYSQL_HOST', '127.0.0.1'),
        'user': os.environ.get('MYSQL_USER', 'vagrant'),
        'password': os.environ.get('MYSQL_PASSWORD', 'vagrant'),
        'database': os.environ.get('MYSQL_DB', 'thanatos'),
    }

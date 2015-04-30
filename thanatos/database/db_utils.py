

import os
import bz2
import urllib
import MySQLdb
import logging

_log = logging.getLogger('thanatos.database.db_utils')

# Base URL for where to download SQL tables from
# Using Fuzztsteve's site for now
_base_url = 'https://www.fuzzwork.co.uk/dump/latest/'

# File extension to be used in the download, save, and loading
_table_file_extension = '.sql.bz2'

# A list of all tables required by the different procs.
# If adding a new proc make sure it's required tables are listed here.
_required_tables = [
    'dgmTypeAttributes',
    'invTypes',
    'invGroups',
    'invCategories',
    'mapRegions',
    'mapRegionJumps',
]


def execute_sql(sql, db_connection, fetch_one=False):
    """

    :param sql:
    :param db_connection:

    :return:
    """

    cursor = db_connection.cursor()

    cursor.execute(sql)

    if fetch_one:
        return cursor.fetchone()

    return [x for x in cursor.fetchall()]


def update_sql_stored_procs(db_connection):
    """

    :param db_connection:

    :return:
    """

    sql_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sql')

    for sql_file_name in os.listdir(sql_dir_path):
        _log.info('Running {}'.format(sql_file_name))

        cursor = db_connection.cursor()

        sql_file_path = os.path.join(sql_dir_path, sql_file_name)
        sql_file = open(sql_file_path)
        sql = " ".join(sql_file.readlines())

        cursor.execute(sql)
        cursor.close()


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


def load_tables_from_files(db_connection, tables=_required_tables):
    """ Looks in the current working directory for all required tables. """

    _log.info('Loading tables from disk to DB.')

    for table in tables:
        _log.info('Loading the following table: {}'.format(table))

        table_name = table + _table_file_extension

        with bz2.BZ2File(table_name, 'r') as sql_file:
            sql = sql_file.read()
            execute_sql(sql, db_connection)

    _log.info('Finished loading all requested tables.')


def download_tables(tables_list=_required_tables, base_url=_base_url):
    """ Downloads a given list of tables from a given web site.

    :param tables_list: A list of strings, each a table name to download.
    :type tables_list: list

    :return:
    """

    _log.info('Downloading all required tables.')

    formatting_string = base_url + '{}' + _table_file_extension

    for table in tables_list:
        full_url = formatting_string.format(table)

        _log.info('Downloading {}'.format(full_url))

        urllib.urlretrieve(full_url, table + _table_file_extension)

    _log.info('Finished downloading all required tables.')
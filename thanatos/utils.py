

import bz2
import urllib
import logging

from thanatos.questions.base import Question

_log = logging.getLogger('thanatos.utils')

# Base URL for where to download SQL tables from
# Using Fuzztsteve's site for now
_base_url = 'https://www.fuzzwork.co.uk/dump/latest/'

# File extension to be used in the download, save, and loading
_table_file_extension = '.sql.bz2'


def get_categories():
    """

    :return: A dictionary of sets representing the categories and their sub categories.
    :rtype: dict
    """

    categories = {}

    for subclass in Question.__subclasses__():
        if subclass.category_primary not in categories:
            categories[subclass.category_primary] = {}

        if subclass.category_secondary not in categories[subclass.category_primary]:
            categories[subclass.category_primary][subclass.category_secondary] = {}

        categories[subclass.category_primary][subclass.category_secondary][subclass] = subclass.random_weight



    return categories


def get_list_of_required_tables():
    """ Get a list of all the unique required tables for questions.

    :return: Set of required tables
    :rtype: set
    """

    required_tables = DB.required_tables

    return required_tables


def check_if_required_tables_exist():
    """ Checks if all required tables exist in the DB.

    :return: A list of all missing tables.
    :rtype: list
    """


def load_table_from_file(tables):
    """ Loads a give set of tables from disk and populates the DB with them. """

    db = DB()

    for table in tables:
        table_name = get_table_filename(table)

        with bz2.BZ2File(table_name, 'r') as sql_file:
            sql = sql_file.read()
            db.execute(sql)


def download_tables(tables_list, base_url=_base_url):
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


def get_table_filename(table_name):
    """

    :param table_name: Name of the table we want a filename for.
    :type table_name:

    :return: The filename to be loaded
    :rtype: str
    """

    return table_name + _table_file_extension
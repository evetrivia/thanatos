

import urllib
import logging

from thanatos.questions import Question

_log = logging.getLogger('thanatos.utils')

# Base URL for where to download SQL tables from
# Using Fuzztsteve's site for now
_base_url = 'https://www.fuzzwork.co.uk/dump/latest/'

# File extension to be used in the download, save, and loading
_table_file_extension = '.sql.bz2'


def get_list_of_required_tables():
    """ Get a list of all the unique required tables for questions.

    :return: Set of required tables
    :rtype: set
    """

    required_tables = set()

    for subclass in Question.__subclasses__():
        required_tables.update(subclass.required_tables)

    return required_tables


def check_if_required_tables_exist():
    """ Checks if all required tables exist in the DB.

    :return: A list of all missing tables.
    :rtype: list
    """


def download_tables(tables_list, base_url=_base_url):
    """ Downloads a given list of tables from a given web site.

    :param tables_list: A list of strings, each a table name to download.
    :type tables_list: list

    :return:
    """
    
    _log.info('Downloading all required tables.')
    
    formating_string = base_url + '{}' + _table_file_extension
    list_of_urls     = [formating_string.format(x) for x in tables_list]
    
    for table in tables_list:
        full_url = formating_string.format(table)
        
        _log.info('Downloading {}'.format(full_url))
        
        urllib.urlretrieve(full_url, table + _table_file_extension)
    
    _log.info('Finished downloading all required tables.')


from thanatos.questions import Question

# Base URL for where to download SQL tables from
# Using Fuzztsteve's site for now
_base_url = 'https://www.fuzzwork.co.uk/dump/latest/'


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
    
    formating_string = base_url + '{}' + '.sql.bz2'
    
    list_of_urls = [formating_string.format(x) for x in tables_list]
    
    print list_of_urls
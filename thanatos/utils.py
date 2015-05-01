

import logging

from thanatos.questions.base import Question

_log = logging.getLogger('thanatos.utils')


def get_all_categories():
    """

    :return: A dictionary of sets representing the categories and their sub categories.
    :rtype: dict
    """

    categories = {}
    subclasses = get_question_subclasses()
    
    for subclass in subclasses:
        if subclass.category_primary is not None and subclass.category_secondary is not None:
            if subclass.category_primary not in categories:
                categories[subclass.category_primary] = {}
    
            if subclass.category_secondary not in categories[subclass.category_primary]:
                categories[subclass.category_primary][subclass.category_secondary] = {}
    
            categories[subclass.category_primary][subclass.category_secondary][subclass.__name__] = subclass.random_weight
        
    return categories

def get_question_subclasses():
    return Question.__subclasses__()


import logging

from random import choice
from itertools import repeat

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
                categories[subclass.category_primary] = set()
    
            categories[subclass.category_primary].update(subclass.__name__)
        
    return categories


def get_question_subclasses():
    return Question.__subclasses__()


def get_random_question():
    questions = []
    subclasses = get_question_subclasses()

    for subclass in subclasses:
        questions.extend(repeat(subclass, subclass.random_weight))

    return choice(questions)


def get_question_from_category(primary_category):
    questions = []
    categories = get_all_categories()

    for sub_category in categories[primary_category]:
        for qusetion in categories[primary_category][sub_category]:
            questions.extend(repeat(qusetion, qusetion.random_weight))

    return choice(questions)
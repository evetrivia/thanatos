

import logging

from random import choice
from itertools import repeat

from thanatos.questions.base import Question

_log = logging.getLogger('thanatos.utils')


def get_all_question_details():
    """

    :return: A dictionary of sets representing the categories and their sub categories.
    :rtype: dict
    """

    categories = {}
    subclasses = get_question_subclasses()
    
    for subclass in subclasses:
        if subclass.category is not None and subclass.sub_category is not None:
            name = subclass.__name__.lower()
            category = subclass.category['name'].lower()
            sub_category = subclass.sub_category['name'].lower()
            
            if category not in categories:
                categories[category] = subclass.category
                categories[category]['sub_categories'] = {}
            
            if sub_category not in categories[category]['sub_categories']:
                categories[category]['sub_categories'][sub_category] = subclass.sub_category
                categories[category]['sub_categories'][sub_category]['questions'] = {}
    
            categories[category]['sub_categories'][sub_category]['questions'][name] = {
                'name': subclass.name,
                'description': subclass.description,
                'weight': subclass.random_weight,
                'question': subclass.question,
            }
        
    return categories


def get_question_subclasses():
    return Question.__subclasses__()


def get_random_question():
    questions = []
    subclasses = get_question_subclasses()

    for subclass in subclasses:
        questions.extend(repeat(subclass, subclass.random_weight))

    return choice(questions)


def get_question(question_id):
    subclasses = get_question_subclasses()
    
    for subclass in subclasses:
        if subclass.__name__.lower() == question_id:
            return subclass
    
    raise InvalidQuestionException('The specified question does not exist.')


def get_question_from_category(category):
    questions = []
    subclasses = get_question_subclasses()

    for question in subclasses:
        if question.category is not None and question.sub_category is not None:
            if question.category['name'].lower() == category:
                questions.extend(repeat(question, question.random_weight))

                return choice(questions)

    raise InvalidQuestionCategoryException('The category specified is invalid.')


def get_question_from_sub_category(category, sub_category):
    questions = []
    subclasses = get_question_subclasses()

    for question in subclasses:
        if question.category is not None and question.sub_category is not None:
            if question.category['name'].lower() == category:
                if question.sub_category['name'].lower() == sub_category:
                    questions.extend(repeat(question, question.random_weight))

                    return choice(questions)

    raise InvalidQuestionCategoryException('Either the category or sub-category specified is invalid.')


class InvalidQuestionCategoryException(Exception):
    pass


class InvalidQuestionException(Exception):
    pass

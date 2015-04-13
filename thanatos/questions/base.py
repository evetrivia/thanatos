

import logging

from abc import ABCMeta, abstractmethod

_log = logging.getLogger('thanatos.questions.base')


class Question(object):
    """ The base class that all questions are subclasses of. """

    __metaclass__ = ABCMeta

    required_tables = None

    category_primary   = None
    category_secondary = None

    random_weight = 0

    question = None

    @abstractmethod
    def ask(self):
        """ ask is called whenever attempting to get the details of a question.

        The dictionary returned should look like the following example:

        {
            'answer'   : 000,
            'question' : 'What region borders {}?,
            'choices'  : [
                (000, 'Region 000'),
                (001, 'Region 001'),
                (002, 'Region 002'),
            ],
        }

        :return: A dictionary of answer, question, and other details.
        :rtype: dict
        """

        pass
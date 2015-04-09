

import logging

from abc import ABCMeta, abstractmethod

_log = logging.getLogger('thanatos.questions')


class Question(object):
    """ The base class that all questions are subclasses of. """

    __metaclass__ = ABCMeta

    required_tables = None

    def __init__(self):
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


class BorderingRegionsQuestion(Question):
    """ Asks what region boards another given region. """

    required_tables = [
        'mapRegions',
        'mapRegionJumps',
    ]

    def __init__(self):
        question = 'Which of the following regions borders the {} region?'

        super(Question, self).__init__()

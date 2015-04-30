

import random
import logging

from abc import ABCMeta, abstractmethod

_log = logging.getLogger('thanatos.questions.base')


class Question(object):
    """ The base class that all questions are subclasses of. """

    __metaclass__ = ABCMeta

    required_tables = None

    category_primary = None
    category_secondary = None

    random_weight = 0

    question = None

    @abstractmethod
    def ask(self):
        """ ask is called whenever attempting to get the details of a question.

        The dictionary returned should look like the following example:

        {
            'answer'   : 000,
            'question' : 'What region borders {}?',
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

    def format_question(self, correct_answer, possible_wrong_answers, question):
        """ Takes a set of values and converts it to the standard format
        expected as a return from self.ask().

        :param correct_answer: A tuple of the answer key and text to be shown.
        :type correct_answer: tuple

        :param possible_wrong_answers: A list of tuples, each tuple being being
        (id, display_name).
        :type possible_wrong_answers: list

        :param question: A string to be set as the question that is asked.
        :type question: string

        :return: A dict that matches what is expected as the return value for self.ask()
        :rtype: dict
        """

        # Lets randomly select some wrong answers
        wrong_answers = random.sample(possible_wrong_answers, 2)

        # Combine the selected wrong answers with the actual answer and shuffle
        choices = [x for x in wrong_answers]
        choices.append(correct_answer)
        random.shuffle(choices)

        # Format it all in a nice dict
        question = {
            'answer': correct_answer[0],
            'question': question,
            'choices': self.convert_choices_to_dict(choices)
        }

        return question

    @staticmethod
    def convert_choices_to_dict(choices):
        """ Takes a list of tuples and converts it to a list of dictionaries of
        where each dictionary has a value and text key. This is the expected format
        of question choices to be returned by self.ask()

        :param convert_choices_to_dict:
        :type convert_choices_to_dict: list

        :return:
        :rtype:
        """

        formatted_choices = []

        for x in choices:
            formatted_choices.append({
                'value': x[0],
                'text': x[1],
            })

        return formatted_choices


class TestableBaseQuestion(Question):
    """ A subclass of the base class to test against. """

    def ask(self):
        pass

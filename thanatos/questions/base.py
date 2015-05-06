

import random
import logging

from abc import ABCMeta, abstractmethod

from thanatos.ccp_image_server import get_type_links

_log = logging.getLogger('thanatos.questions.base')


class Question(object):
    """ The base class that all questions are subclasses of. """

    __metaclass__ = ABCMeta

    name = None
    question = None
    description = None
    random_weight = 0
    category = None
    sub_category = None

    def __init__(self, db_connection):
        self.db_connection = db_connection

    @abstractmethod
    def ask(self):
        """ ask is called whenever attempting to get a question.

        :return: A dictionary of answer, question, and other details.
        :rtype: dict
        """

        pass

    def format_question(self, correct_answer, possible_wrong_answers, question, add_images_to_question=False):
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

        if add_images_to_question is True:
            question['images'] = get_type_links(correct_answer[0])

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

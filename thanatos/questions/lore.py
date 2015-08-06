

import random
import logging

from thanatos import categories, lore
from thanatos.questions.base import Question

_log = logging.getLogger('thanatos')


def get_random_weight(questions):
    weight = len(questions) / 4

    if weight > 1:
        return weight

    else:
        return 1


class CapsuleerLoreQuestion(Question):
    """ Asks questions about capsuleer created lore. """

    name = 'Capsuleer Lore'
    description = 'Asks questions about capsuleer created lore.'
    category = categories.lore
    sub_category = categories.lore_capsuleer

    random_weight = get_random_weight(lore.capsuleer_lore_questions)

    question = 'Capsuleer lore questions.'

    def ask(self):
        raw_question = random.choice(lore.capsuleer_lore_questions)

        correct_answer = (0, raw_question['answer'])

        possible_wrong_answers = [(x, raw_question['wrong_answers'][x]) for x in xrange(0, len(raw_question['wrong_answers']))]

        question = self.format_question(correct_answer, possible_wrong_answers, raw_question['question'])

        return question


class NPCLoreQuestion(Question):
    """ Asks questions about capsuleer created lore. """

    name = 'NPC Lore'
    description = 'Asks questions about NPC created lore.'
    category = categories.lore
    sub_category = categories.lore_npc

    random_weight = get_random_weight(lore.npc_lore_questions)

    question = 'NPC lore questions.'

    def ask(self):
        raw_question = random.choice(lore.npc_lore_questions)

        correct_answer = (0, raw_question['answer'])

        possible_wrong_answers = [(x, raw_question['wrong_answers'][x]) for x in xrange(0, len(raw_question['wrong_answers']))]

        question = self.format_question(correct_answer, possible_wrong_answers, raw_question['question'])

        return question



import random
import logging

from thanatos.database import inventory
from thanatos.questions.base import Question

_log = logging.getLogger('thanatos.questions.inventory')


class HighSlotsQuestion(Question):
    """ Asks what region boards another given region. """

    category_primary = 'Inventory'
    category_secondary = 'Slots'

    random_weight = 10

    question = 'How many high slots does the {} have?'

    high_slots_dogma_attribute = 14

    slots_min = 0
    slots_max = 9  # 1 more than the max of 8 do to how range works

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def ask(self):
        all_ships = inventory.get_all_published_ships_basic(self.db_connection)

        chosen_ship = random.choice(all_ships)

        high_slots = int(inventory.get_dogma_attribute_for_type(
            self.db_connection,
            chosen_ship[0],
            self.high_slots_dogma_attribute)
        )

        correct_answer = (high_slots, high_slots)

        possible_answers = range(self.slots_min, self.slots_max)
        possible_wrong_answers = list(set(possible_answers) - set([correct_answer[0]]))
        possible_wrong_answers = [(x, x) for x in possible_wrong_answers]

        question = self.format_question(correct_answer, possible_wrong_answers, self.question.format(chosen_ship[1]))

        return question

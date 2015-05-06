

import random
import logging

from thanatos import categories
from thanatos.database import inventory
from thanatos.questions.base import Question

_log = logging.getLogger('thanatos.questions.inventory')


class SlotsQuestion(Question):
    """ Asks what region boards another given region. """

    name = 'Slots Question'
    description = 'Asks how many high/mid/low/turret/launcher slots a given ship has.'
    category = categories.inventory
    sub_category = categories.inventory_slots

    random_weight = 10

    question = 'How many {} slots does the {} have?'

    high_slots_dogma_attribute = 14

    slots = {
        'high': 14,
        'mid': 13,
        'low': 12,
        'launcher': 101,
        'turret': 102,
    }

    slots_min = 0
    slots_max = 9  # 1 more than the max of 8 due to how range works

    def ask(self):
        all_ships = inventory.get_all_published_ships_basic(self.db_connection)
        chosen_ship = random.choice(all_ships)
        chosen_slot = random.choice(self.slots.keys())

        high_slots = int(inventory.get_dogma_attribute_for_type(
            self.db_connection,
            chosen_ship[0],
            self.slots[chosen_slot])
        )

        correct_answer = (high_slots, high_slots)

        possible_answers = range(self.slots_min, self.slots_max)
        possible_wrong_answers = list(set(possible_answers) - set([correct_answer[0]]))
        possible_wrong_answers = [(x, x) for x in possible_wrong_answers]

        question = self.format_question(correct_answer, possible_wrong_answers, self.question.format(chosen_slot, chosen_ship[1]))

        return question

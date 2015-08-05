

import random
import logging

from thanatos import categories
from thanatos.database import inventory
from thanatos.questions.base import Question

_log = logging.getLogger('thanatos')


class SlotsQuestion(Question):
    """ Asks what region boards another given region. """

    name = 'Slots Question'
    description = 'Asks how many high/mid/low/turret/launcher slots a given ship has.'
    category = categories.inventory
    sub_category = categories.inventory_slots

    random_weight = 20

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
        chosen_slot = random.choice(self.slots.keys())

        # Go into a while loop until we get a ship that actually has a value for the chosen dogma attribute
        while True:
            chosen_ship = random.choice(all_ships)

            slot_count = inventory.get_dogma_attribute_for_type(
                self.db_connection,
                chosen_ship[0],
                self.slots[chosen_slot]
            )

            if slot_count is not None:
                correct_answer = (int(slot_count), int(slot_count))

                possible_answers = range(self.slots_min, self.slots_max)
                possible_wrong_answers = list(set(possible_answers) - set([correct_answer[0]]))
                possible_wrong_answers = [(x, x) for x in possible_wrong_answers]

                question = self.format_question(correct_answer, possible_wrong_answers, self.question.format(chosen_slot, chosen_ship[1]))

                return question


class ShipImageIdentificationQuestion(Question):
    """ Asks the user to select the correct ship based on an image server link. """

    name = 'Ship Image Identification'
    description = 'Pick what ship is shown in the provided image.'
    category = categories.inventory
    sub_category = categories.inventory_ship_id

    random_weight = 16

    question = 'What ship is pictured?'

    def ask(self):
        all_ships = inventory.get_all_published_ships_basic(self.db_connection)
        chosen_ship = random.choice(all_ships)

        possible_wrong_answers = list(set(all_ships) - set([chosen_ship]))
        possible_wrong_answers = [(x[0], x[1]) for x in possible_wrong_answers]

        question = self.format_question(chosen_ship, possible_wrong_answers, self.question, add_images_to_question=True)

        return question


class ShipImageIdentificationHardQuestion(Question):
    """ Asks the user to select the correct ship based on an image server link but
    the answers are all variations of the same hull. """

    name = 'Ship Image Identification (Hard)'
    description = 'Pick what ship is shown in the provided image.'
    category = categories.inventory
    sub_category = categories.inventory_ship_id_hard

    random_weight = 8

    question = 'What ship is pictured?'

    def ask(self):
        ships_with_variations = inventory.get_ships_that_have_variations(self.db_connection)
        chosen_hull = random.choice(ships_with_variations)

        possible_ships = inventory.get_type_variations(self.db_connection, chosen_hull[0])
        chosen_ship = random.choice(possible_ships)

        possible_wrong_answers = list(set(possible_ships) - set([chosen_ship]))
        possible_wrong_answers = [(x[0], x[1]) for x in possible_wrong_answers]

        question = self.format_question(chosen_ship, possible_wrong_answers, self.question, add_images_to_question=True)

        return question

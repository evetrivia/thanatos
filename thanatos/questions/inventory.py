

import logging

from random import choice, sample

from thanatos.questions.base import Question

_log = logging.getLogger('thanatos.questions.inventory')


class HighSlotsQuestion(Question):
    """ Asks what region boards another given region. """

    category_primary   = 'Inventory'
    category_secondary = 'Slots'

    random_weight = 10

    question = 'How many high slots does the {} have?'

    def __init__(self, database):
        self.db = database

    def ask(self):
        # Get a list of all ships in the game
        all_ships = self.db.get_all_published_ships_basic()
        print all_ships

        # Get the specified dogma attribute for the selected ship

        #




        return None
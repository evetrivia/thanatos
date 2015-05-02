

import random
import logging

from thanatos import categories
from thanatos.database import universe
from thanatos.questions.base import Question

_log = logging.getLogger('thanatos.questions.universe')


class BorderingRegionsQuestion(Question):
    """ Asks what region boards another given region. """

    name = 'Bordering Regions'
    description = 'Asks what region borders another region.'
    category = categories.geography
    sub_category = categories.geography_regions

    random_weight = 10

    question = 'Which of the following regions borders the {} region?'

    def ask(self):
        # Lets start by getting a region to base this all on and call it the source region
        # Lets ignore WH regions though
        all_regions = universe.get_all_not_wh_regions(self.db_connection)

        # Before we pick our source region we need to remove the Jove regions of as they have no gates:
        all_regions = remove_regions_with_no_gates(all_regions)

        # Now pick our random source region
        source_region = random.choice(all_regions)

        # Next lets find a random region that is connected to the source region, this will be the answer
        connected_regions = universe.get_all_regions_connected_to_region(self.db_connection, source_region[0])
        correct_answer = random.choice(connected_regions)

        # Now we need to find the possible wrong answers
        # These regions need to not be connected to the source region
        # And also not the source region itself
        regions_to_exclude = [x for x in connected_regions]
        regions_to_exclude.append(source_region)

        possible_wrong_answers = list(set(all_regions) - set(regions_to_exclude))

        question = self.format_question(correct_answer, possible_wrong_answers, self.question.format(source_region[1]))

        return question


class PoitotFamousForQuestion(Question):
    """ Asks what Poitot is famous for being. """

    name = 'Poitot'
    description = 'Asks what the Poitot solar system is famous for being.'
    category = categories.geography
    sub_category = categories.geography_miscellaneous

    random_weight = 1

    question = 'Poitot is famous for being...?'

    def ask(self):
        correct_answer = (0, 'The only named system in Syndicate.')

        # It would be great to add more here over time.
        possible_wrong_answers = [
            (1, 'Kind to animals.'),
            (2, 'A fictional space detective.'),
            (3, 'Adjacent to F67E-Q.'),
        ]

        question = self.format_question(correct_answer, possible_wrong_answers, self.question)

        return question


def remove_regions_with_no_gates(regions):
    """ Removes all Jove regions from a list of regions.

    :param regions: A list of tuples (regionID, regionName)
    :type regions: list

    :return: A list of regions minus those in jove space
    :rtype: list
    """

    list_of_gateless_regions = [
        (10000004, 'UUA-F4'),
        (10000017, 'J7HZ-F'),
        (10000019, 'A821-A'),
    ]

    for gateless_region in list_of_gateless_regions:
        if gateless_region in regions:
            regions.remove(gateless_region)

    return regions



from random import choice, sample

from thanatos.database       import DB
from thanatos.questions.base import Question


class BorderingRegionsQuestion(Question):
    """ Asks what region boards another given region. """

    category_primary   = 'Geography'
    category_secondary = 'Regions'

    random_weight = 10

    question = 'Which of the following regions borders the {} region?'

    def __init__(self):
        self.db = DB()

    def ask(self):
        # Lets start by getting a region to base this all on and call it the source region
        # Lets ignore WH regions though
        all_regions   = self.db.get_all_not_wh_regions()
        source_region = choice(all_regions)

        # Next lets find a random region that is connected to the source region, this will be the answer
        connected_regions = self.db.get_all_regions_connected_to_region(source_region[0])
        correct_answer    = choice(connected_regions)

        # Now we need to find the other wrong answers
        # These regions need to not be connected to the source region
        # And also not the source region itself
        # And again lets ignore WH regions, 11000000 and up
        regions_to_exclude = [str(x[0]) for x in connected_regions]
        regions_to_exclude.append(str(source_region[0]))

        sql = """
            SELECT mapRegions.regionID, mapRegions.regionName
              FROM mapRegions
             WHERE mapRegions.regionID NOT IN ({})
               AND mapRegions.regionID < 11000000
        """.format(','.join(regions_to_exclude))

        wrong_answers = sample(self.db.execute(sql), 2)

        question = self.format_question(correct_answer, wrong_answers, self.question.format(correct_answer[1]))

        return question


class PoitotFamousForQuestion(Question):
    """ Asks what Poitot is famous for being. """

    category_primary   = 'Geography'
    category_secondary = 'Miscellaneous'

    random_weight = 1

    question = 'Poitot is famous for being...?'

    def ask(self):
        correct_answer   = (0, 'The only named system in Syndicate.')
        wrong_answers = [
            (1, 'Kind to animals.'),
            (2, 'A fictional space detective.'),
            (3, 'Adjacent to F67E-Q.'),
        ]

        question = self.format_question(correct_answer, wrong_answers, self.question)

        return question


from thanatos.database       import DB
from thanatos.questions.base import Question


class BorderingRegionsQuestion(Question):
    """ Asks what region boards another given region. """

    required_tables = [
        'mapRegions',
        'mapRegionJumps',
    ]

    category_primary   = 'Geography'
    category_secondary = 'Regions'

    random_weight = 50

    question = 'Which of the following regions borders the {} region?'

    def __init__(self):
        self.db = DB().connection

    def ask(self):
        pass

    def _sql_loopup(self):
        cursor = self.db.cursor()

        # Lets start by getting a region to base this all on and call it the source region
        # Lets ignore WH regions though, 11000000 and up
        sql = """
            SELECT regionID, regionName
              FROM mapRegions
             WHERE regionID < 11000000
             ORDER BY RAND()
             LIMIT 1
        """

        cursor.execute(sql)

        source_region_id, source_region_name = cursor.fetchone()

        # Next lets find a random region that is connected to the source region, this will be the answer
        sql = """
            SELECT toRegionID, regionName
              FROM mapRegionJumps
             INNER JOIN mapRegions ON mapRegionJumps.toRegionID = mapRegions.regionID
             WHERE fromRegionID = {}
             ORDER BY RAND()
             LIMIT 1
        """.format(source_region_id)

        cursor.execute(sql)

        correct_answer = cursor.fetchall()

        # Now we need to find the other wrong answers
        # These regions need to not be connected to the source region
        # And also not the source region itself
        # And again lets ignore WH regions, 11000000 and up
        sql = """
            SELECT regionID, regionName
              FROM mapRegions
             WHERE regionID < 11000000
               AND regionID
        """
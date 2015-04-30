DROP PROCEDURE IF EXISTS get_all_not_wh_regions;

CREATE PROCEDURE `get_all_not_wh_regions` ()
DETERMINISTIC
BEGIN
  SELECT mapRegions.regionID, mapRegions.regionName
    FROM mapRegions
   WHERE mapRegions.regionID < 11000000;
END
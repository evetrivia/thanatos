CREATE PROCEDURE `get_all_regions` ()
DETERMINISTIC
BEGIN
  SELECT mapRegions.regionID, mapRegions.regionName
    FROM mapRegions;
END
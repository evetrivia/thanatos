DROP PROCEDURE IF EXISTS get_all_regions_connected_to_region;

CREATE PROCEDURE `get_all_regions_connected_to_region` (IN paramFromRegionID INTEGER)
DETERMINISTIC
BEGIN
  SELECT mapRegionJumps.toRegionID AS regionID, mapRegions.regionName
    FROM mapRegionJumps
    LEFT JOIN mapRegions ON mapRegions.regionID = mapRegionJumps.toRegionID
   WHERE mapRegionJumps.fromRegionID = paramFromRegionID;
END
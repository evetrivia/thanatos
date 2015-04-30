DROP PROCEDURE IF EXISTS get_all_published_ships_basic;

CREATE PROCEDURE `get_all_published_ships_basic` ()
DETERMINISTIC
BEGIN
  SELECT invTypes.typeID, invTypes.typeName,
         invGroups.groupID, invGroups.groupName,
         invCategories.categoryID, invCategories.categoryName
    FROM invTypes
   INNER JOIN invGroups ON invTypes.groupID = invGroups.groupID
   INNER JOIN invCategories ON invGroups.categoryID = invCategories.categoryID
   WHERE invCategories.categoryID = 6
     AND invTypes.published = 1;
END
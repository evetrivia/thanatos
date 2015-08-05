CREATE PROCEDURE `get_ships_that_have_variations` ()
DETERMINISTIC
BEGIN
  SELECT invTypes.typeID, invTypes.typeName
    FROM invTypes
   INNER JOIN invGroups ON invTypes.groupID = invGroups.groupID
   INNER JOIN invCategories ON invGroups.categoryID = invCategories.categoryID
   INNER JOIN invMetaTypes ON invTypes.typeID=invMetaTypes.parentTypeID
   WHERE invCategories.categoryID = 6
     AND invTypes.published = 1
     AND invTypes.typeID != 672 -- Fuck the Caldari Shuttle, remove that at the proc level
   GROUP BY invTypes.typeID, invTypes.typeName,
            invGroups.groupID, invGroups.groupName,
            invCategories.categoryID, invCategories.categoryName
  HAVING COUNT(invMetaTypes.typeID)>=2;
END
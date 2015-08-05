CREATE PROCEDURE `get_variations_for_type_id` (IN typeID INTEGER)
DETERMINISTIC
BEGIN
  SELECT invTypes.typeID, invTypes.typeName
    FROM invTypes
    LEFT JOIN invMetaTypes ON invTypes.typeID = invMetaTypes.typeID
    WHERE invMetaTypes.parentTypeID = typeID
       OR invTypes.typeID = typeID;
END
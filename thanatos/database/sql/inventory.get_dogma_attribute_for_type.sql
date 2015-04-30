DROP PROCEDURE IF EXISTS get_dogma_attribute_for_type;

CREATE PROCEDURE `get_dogma_attribute_for_type` (IN paramTypeID INTEGER, IN paramAttrID INTEGER)
DETERMINISTIC
BEGIN
  SELECT COALESCE(dgmTypeAttributes.valueInt, dgmTypeAttributes.valueFloat)
    FROM invTypes
    LEFT JOIN dgmTypeAttributes ON invTypes.typeID = dgmTypeAttributes.typeID
   WHERE invTypes.typeID = paramTypeID
     AND dgmTypeAttributes.attributeID = paramAttrID;
END
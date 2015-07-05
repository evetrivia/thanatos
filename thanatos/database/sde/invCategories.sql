-- MySQL dump 10.13  Distrib 5.6.12, for Linux (x86_64)
--
-- Host: localhost    Database: sdecarnyx1
-- ------------------------------------------------------
-- Server version	5.6.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `invCategories`
--

DROP TABLE IF EXISTS `invCategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invCategories` (
  `categoryID` int(11) NOT NULL,
  `categoryName` varchar(100) DEFAULT NULL,
  `description` varchar(3000) DEFAULT NULL,
  `iconID` int(11) DEFAULT NULL,
  `published` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`categoryID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invCategories`
--

LOCK TABLES `invCategories` WRITE;
/*!40000 ALTER TABLE `invCategories` DISABLE KEYS */;
INSERT INTO `invCategories` VALUES (0,'#System',NULL,NULL,0),(1,'Owner',NULL,NULL,0),(2,'Celestial',NULL,NULL,1),(3,'Station',NULL,NULL,0),(4,'Material',NULL,22,1),(5,'Accessories',NULL,33,1),(6,'Ship',NULL,NULL,1),(7,'Module',NULL,67,1),(8,'Charge',NULL,NULL,1),(9,'Blueprint',NULL,21,1),(10,'Trading',NULL,NULL,0),(11,'Entity',NULL,NULL,0),(14,'Bonus',NULL,0,0),(16,'Skill',NULL,33,1),(17,'Commodity',NULL,0,1),(18,'Drone',NULL,0,1),(20,'Implant',NULL,0,1),(22,'Deployable',NULL,0,1),(23,'Starbase',NULL,0,1),(24,'Reaction',NULL,0,1),(25,'Asteroid',NULL,NULL,1),(26,'WorldSpace',NULL,NULL,0),(29,'Abstract',NULL,NULL,0),(30,'Apparel',NULL,NULL,1),(32,'Subsystem',NULL,NULL,1),(34,'Ancient Relics',NULL,NULL,1),(35,'Decryptors',NULL,NULL,1),(39,'Infrastructure Upgrades',NULL,NULL,1),(40,'Sovereignty Structures',NULL,NULL,1),(41,'Planetary Interaction',NULL,NULL,1),(42,'Planetary Resources',NULL,NULL,1),(43,'Planetary Commodities',NULL,NULL,1),(46,'Orbitals',NULL,NULL,1),(49,'Placeables',NULL,NULL,0),(53,'Effects',NULL,NULL,0),(54,'Lights',NULL,NULL,0),(59,'Cells',NULL,NULL,0),(63,'Special Edition Assets',NULL,NULL,1),(65,'Structure',NULL,NULL,1),(350001,'Infantry',NULL,NULL,0);
/*!40000 ALTER TABLE `invCategories` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-06-02 21:29:14

-- MySQL dump 10.13  Distrib 5.7.16, for Linux (x86_64)
--
-- Host: localhost    Database: Courses
-- ------------------------------------------------------
-- Server version	5.7.16-0ubuntu0.16.04.1

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
-- Table structure for table `enrollment`
--

DROP TABLE IF EXISTS `enrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `enrollment` (
  `course` varchar(20) DEFAULT NULL,
  `enrollment_total` int(11) DEFAULT NULL,
  `enrollment_capacity` int(11) DEFAULT NULL,
  `time_stamp` date DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollment`
--

LOCK TABLES `enrollment` WRITE;
/*!40000 ALTER TABLE `enrollment` DISABLE KEYS */;
INSERT INTO `enrollment` VALUES ('cs/240',357,370,'2017-01-08','09:00:02'),('cs/241',356,400,'2017-01-08','09:00:02'),('cs/251',295,320,'2017-01-08','09:00:02'),('co/481',16,17,'2017-01-08','09:00:02'),('econ/102',980,1110,'2017-01-08','09:00:02'),('co/444',8,10,'2017-01-08','09:00:02'),('biol/355',280,280,'2017-01-08','09:00:02'),('clas/104',674,675,'2017-01-08','09:00:02'),('biol/450',80,80,'2017-01-08','09:00:02'),('kin/310',38,40,'2017-01-08','09:00:02'),('ahs/100',106,344,'2017-01-08','09:00:02'),('hlth/340',85,90,'2017-01-08','09:00:02'),('chem/267',359,446,'2017-01-08','09:00:02'),('cs/452',30,40,'2017-01-08','09:00:02'),('math/136',1142,1668,'2017-01-08','09:00:02'),('math/239',360,360,'2017-01-08','09:00:02'),('math/138',1370,1717,'2017-01-08','09:00:02'),('phys/122',310,500,'2017-01-08','09:00:02'),('cs/136',884,990,'2017-01-08','09:00:02'),('econ/101',1248,1290,'2017-01-08','09:00:02'),('math/128',723,880,'2017-01-08','09:00:02'),('math/127',324,340,'2017-01-08','09:00:02');
/*!40000 ALTER TABLE `enrollment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-08 11:03:58

-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: ftable
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `history_log`
--

DROP TABLE IF EXISTS `history_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login` varchar(60) DEFAULT NULL,
  `logout` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history_log`
--

LOCK TABLES `history_log` WRITE;
/*!40000 ALTER TABLE `history_log` DISABLE KEYS */;
INSERT INTO `history_log` VALUES (1,'yosri Log in at 2021-12-31 in Time: 20:46:25.787133',NULL),(2,'yosri Log in at 2021-12-31 in Time: 22:42:43.067161',NULL),(3,'yosri Log in at 2021-12-31 in Time: 22:44:14.019638',NULL),(4,'yosri Log in at 2021-12-31 in Time: 23:03:25.090491',NULL),(5,'yosri Log in at 2021-12-31 in Time: 23:05:03.536821',NULL),(6,'yosri Log in at 2021-12-31 in Time: 23:05:03.536821',NULL),(7,'yosri Log in at 2021-12-31 in Time: 23:08:42.191491',NULL),(8,'yosri Log in at 2021-12-31 in Time: 23:36:57.826244',NULL),(9,'yosri Log in at 2021-12-31 in Time: 23:36:57.826244',NULL),(10,NULL,'yosri Log out at 2021-12-31 in Time: 23:36:57.826244'),(11,'yosri Log in at 2021-12-31 in Time: 23:45:18.629749',NULL),(12,'ABDELHAMED Log in at 2022-01-01 in Time: 08:52:51.807797',NULL),(13,'ABDELHAMED Log in at 2022-01-01 in Time: 08:52:51.807797',NULL),(14,'YOSRI Log in at 2022-01-01 in Time: 08:59:08.732439',NULL);
/*!40000 ALTER TABLE `history_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-01  9:00:46

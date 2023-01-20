-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 10.10.21.105    Database: obokmoolsan
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `balance_sheet`
--

DROP TABLE IF EXISTS `balance_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `balance_sheet` (
  `매출` varchar(45) DEFAULT NULL,
  `지출` varchar(45) DEFAULT NULL,
  `순이익` varchar(45) DEFAULT NULL,
  `날짜` varchar(45) NOT NULL,
  PRIMARY KEY (`날짜`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `balance_sheet`
--

LOCK TABLES `balance_sheet` WRITE;
/*!40000 ALTER TABLE `balance_sheet` DISABLE KEYS */;
INSERT INTO `balance_sheet` VALUES ('660000','318200','281800','2023-01-18'),('168000','83440','84560','2023-01-19');
/*!40000 ALTER TABLE `balance_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bom`
--

DROP TABLE IF EXISTS `bom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bom` (
  `메뉴코드` varchar(45) DEFAULT NULL,
  `요리` varchar(45) DEFAULT NULL,
  `재료이름` varchar(45) DEFAULT NULL,
  `재료코드` varchar(45) DEFAULT NULL,
  `수량` varchar(45) DEFAULT NULL,
  `단위` varchar(45) DEFAULT NULL,
  `단가` varchar(45) DEFAULT NULL,
  KEY `1_idx` (`메뉴코드`),
  CONSTRAINT `1` FOREIGN KEY (`메뉴코드`) REFERENCES `menulist` (`메뉴코드`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bom`
--

LOCK TABLES `bom` WRITE;
/*!40000 ALTER TABLE `bom` DISABLE KEYS */;
INSERT INTO `bom` VALUES ('m100','간장게장','간장','c001','600','ml','1800'),('m100','간장게장','꽃게','c006','1','kg','10000'),('m100','간장게장','사과','c018','400','g','2000'),('m100','간장게장','생강가루','c020','15','ml','150'),('m100','간장게장','소주 ','c024','45','ml','270'),('m100','간장게장','청양고추','c031','40','g','320'),('m100','간장게장','통마늘','c034','500','g','5000'),('m100','간장게장','풋고추','c035','20','g','100'),('m200','해물찜','고춧가루','c004','90','g','2700'),('m200','해물찜','관자','c005','100','g','6000'),('m200','해물찜','다시마','c007','10','g','300'),('m200','해물찜','다진 마늘','c008','15','g','45'),('m200','해물찜','다진 생강','c009','5','g','150'),('m200','해물찜','다진 파','c010','30','g','90'),('m200','해물찜','멸치','c015','20','g','200'),('m200','해물찜','새우','c019','200','g','4800'),('m200','해물찜','설탕','c022','10','g','10'),('m200','해물찜','소금','c023','15','g','15'),('m200','해물찜','오징어','c028','180','g','1260'),('m200','해물찜','전분','c029','30','g','45'),('m200','해물찜','참기름','c030','10','ml','100'),('m200','해물찜','콩나물','c032','500','g','1500'),('m300','고등어조림','고등어','c002','2','팩','3000'),('m300','고등어조림','고추장','c003','15','g','30'),('m300','고등어조림','고춧가루','c004','30','g','900'),('m300','고등어조림','다진 마늘','c008','15','g','45'),('m300','고등어조림','대파','c012','20','g','100'),('m300','고등어조림','된장','c013','15','g','26'),('m300','고등어조림','맛술','c014','45','ml','225'),('m300','고등어조림','무','c016','200','g','300'),('m300','고등어조림','물엿','c017','15','ml','27'),('m300','고등어조림','설탕','c022','15','g','15'),('m300','고등어조림','양파','c026','300','g','450'),('m300','고등어조림','청양고추','c031','20','g','160'),('m400','서대회','고추장','c003','45','g','90'),('m400','서대회','고춧가루','c004','30','g','900'),('m400','서대회','다진 마늘','c008','15','g','45'),('m400','서대회','다진 생강','c009','5','g','150'),('m400','서대회','다진 파','c010','30','g','90'),('m400','서대회','대파','c012','20','g','100'),('m400','서대회','무','c016','100','g','150'),('m400','서대회','서대','c021','500','g','3000'),('m400','서대회','설탕','c022','30','g','30'),('m400','서대회','소금','c023','10','g','10'),('m400','서대회','식초','c025','45','ml','45'),('m400','서대회','청양고추','c031','10','g','80'),('m400','서대회','풋고추','c035','10','g','50'),('m500','오징어 초무침','간장','c001','50','ml','150'),('m500','오징어 초무침','고추장','c003','5','g','10'),('m500','오징어 초무침','고춧가루','c004','15','g','450'),('m500','오징어 초무침','다진 마늘','c008','5','g','15'),('m500','오징어 초무침','당근','c011','200','g','600'),('m500','오징어 초무침','설탕','c022','20','g','20'),('m500','오징어 초무침','식초','c025','20','ml','20'),('m500','오징어 초무침','양파','c026','600','g','900'),('m500','오징어 초무침','오이','c027','600','g','2400'),('m500','오징어 초무침','오징어','c028','180','g','1260'),('m500','오징어 초무침','참기름','c030','5','ml','50'),('m500','오징어 초무침','통깨','c033','10','g','85'),('m500','aa','aa','aac11','10','kg','10000');
/*!40000 ALTER TABLE `bom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inquiry_manage`
--

DROP TABLE IF EXISTS `inquiry_manage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inquiry_manage` (
  `문의번호` int NOT NULL AUTO_INCREMENT,
  `주문번호` varchar(45) DEFAULT NULL,
  `제품명` varchar(45) DEFAULT NULL,
  `제품코드` varchar(45) DEFAULT NULL,
  `상태` varchar(45) DEFAULT NULL,
  `회원ID` varchar(45) DEFAULT NULL,
  `문의내용` varchar(600) DEFAULT NULL,
  `답장내용` varchar(600) DEFAULT NULL,
  PRIMARY KEY (`문의번호`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inquiry_manage`
--

LOCK TABLES `inquiry_manage` WRITE;
/*!40000 ALTER TABLE `inquiry_manage` DISABLE KEYS */;
INSERT INTO `inquiry_manage` VALUES (1,'1','간장게장','M100','접수','rlarlxo','상했어요',''),(2,'','간장게장','M100','접수','chlwlgur','몇명이서 먹을수 있나요?',''),(9,'6','해물찜','M200','접수','chlwlgur','Test','Test'),(21,'256','서대회','m400','접수','admin','Test','Test'),(22,'35','고등어조림','m300','접수','chlwlgur','Test','Test'),(23,'29','고등어조림','m300','접수','chlwlgur','Test','Test'),(24,'246','해물찜','m200','접수','admin','Test','Test'),(25,'264','간장게장','m100','접수','chlwlgur','Test','Test'),(26,'15','고등어조림','m300','접수','chlwlgur','Test','Test'),(27,'291','해물찜','m200','접수','chlwlgur','Test','Test'),(28,'277','간장게장','m100','접수','chlwlgur','Test','Test'),(29,'37','고등어조림','m300','접수','chlwlgur','Test','Test'),(30,'293','해물찜','m200','접수','chlwlgur','Test','Test'),(31,'244','간장게장','m100','접수','admin','Test','Test'),(32,'242','오징어 초무침','m500','접수','admin','Test','Test'),(33,'292','고등어조림','m300','접수','chlwlgur','Test','Test'),(34,'292','고등어조림','m300','접수','chlwlgur','Test','Test'),(35,'16','서대회','m400','접수','chlwlgur','Test','Test'),(36,'245','고등어조림','m300','접수','admin','Test','Test'),(37,'257','고등어조림','m300','접수','admin','Test','Test'),(38,'284','서대회','m400','접수','chlwlgur','Test','Test'),(39,'280','간장게장','m100','접수','chlwlgur','Test','Test'),(40,'273','고등어조림','m300','접수','chlwlgur','Test','Test'),(41,'2','간장게장','M100','접수','rlarlxo','Test','Test'),(42,'4','해물찜','M200','접수','chlwlgur','Test','Test'),(43,'14','고등어조림','m300','접수','chlwlgur','Test','Test'),(44,'6','해물찜','M200','접수','chlwlgur','Test','Test'),(45,'5','해물찜','M200','접수','chlwlgur','Test','Test'),(46,'19','오징어 초무침','m500','접수','chlwlgur','Test','Test');
/*!40000 ALTER TABLE `inquiry_manage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `재료코드` varchar(45) NOT NULL,
  `재료이름` varchar(45) DEFAULT NULL,
  `남은수량` varchar(45) DEFAULT NULL,
  `단위` varchar(45) DEFAULT NULL,
  `기준수량` varchar(45) DEFAULT NULL,
  `가격` varchar(45) DEFAULT NULL,
  `단위가격` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`재료코드`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('aac11','aa','20','kg','100000','10000','1000'),('c001','간장','7150','ml','15000','45000','3'),('c002','고등어','20','팩','20','30000','1500'),('c003','고추장','13635','g','14000','28000','2'),('c004','고춧가루','1045','g','2000','60000','30'),('c005','관자','600','g','1000','60000','60'),('c006','꽃게','18','kg','15','150000','10000'),('c007','다시마','760','g','200','6000','30'),('c008','다진 마늘','4275','g','1000','3000','3'),('c009','다진 생강','2880','g','300','9000','30'),('c010','다진 파','280','g','1000','3000','3'),('c011','당근','2400','g','5000','15000','3'),('c012','대파','600','g','1000','5000','5'),('c013','된장','13700','g','14000','23800','1.7'),('c014','맛술','900','ml','1800','9000','5'),('c015','멸치','1520','g','2000','20000','10'),('c016','무','16000','g','20000','30000','1.5'),('c017','물엿','9700','g','10000','18000','1.8'),('c018','사과','5200','g','10000','50000','5'),('c019','새우','1200','g','2000','48000','24'),('c020','생강가루','820','g','1000','10000','10'),('c021','서대','5000','g','5000','30000','6'),('c022','설탕','14200','g','15000','15000','1'),('c023','소금','14640','g','15000','15000','1'),('c024','소주','6960','ml','7500','45000','6'),('c025','식초','14740','ml','15000','15000','1'),('c026','양파','6200','g','20000','30000','1.5'),('c027','오이','2200','g','10000','40000','4'),('c028','오징어','13340','g','20000','140000','7'),('c029','전분','280','g','1000','1500','1.5'),('c030','참기름','1495','ml','1800','18000','10'),('c031','청양고추','120','g','1000','8000','8'),('c032','콩나물','8000','g','10000','30000','3'),('c033','통깨','870','g','1000','8500','8.5'),('c034','통마늘','4000','g','10000','100000','10'),('c035','풋고추','760','g','1000','5000','5');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `max_menu`
--

DROP TABLE IF EXISTS `max_menu`;
/*!50001 DROP VIEW IF EXISTS `max_menu`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `max_menu` AS SELECT 
 1 AS `메뉴코드`,
 1 AS `재료이름`,
 1 AS `수량`,
 1 AS `재료코드`,
 1 AS `남은수량`,
 1 AS `최대개수`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `menulist`
--

DROP TABLE IF EXISTS `menulist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menulist` (
  `메뉴코드` varchar(45) NOT NULL,
  `메뉴명` varchar(45) DEFAULT NULL,
  `가격` int DEFAULT NULL,
  PRIMARY KEY (`메뉴코드`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menulist`
--

LOCK TABLES `menulist` WRITE;
/*!40000 ALTER TABLE `menulist` DISABLE KEYS */;
INSERT INTO `menulist` VALUES ('m100','간장게장',30000),('m200','해물찜',30000),('m300','고등어조림',12000),('m400','서대회',9000),('m500','오징어 초무침',12000);
/*!40000 ALTER TABLE `menulist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordermanage`
--

DROP TABLE IF EXISTS `ordermanage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordermanage` (
  `주문번호` int NOT NULL AUTO_INCREMENT,
  `메뉴명` varchar(45) DEFAULT NULL,
  `주문ID` varchar(45) DEFAULT NULL,
  `수량` varchar(45) DEFAULT NULL,
  `상태` varchar(45) DEFAULT NULL,
  `취소여부` varchar(45) DEFAULT NULL,
  `메뉴코드` varchar(45) DEFAULT NULL,
  `날짜` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`주문번호`),
  KEY `1_idx` (`날짜`),
  KEY `datekey_idx` (`날짜`)
) ENGINE=InnoDB AUTO_INCREMENT=299 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordermanage`
--

LOCK TABLES `ordermanage` WRITE;
/*!40000 ALTER TABLE `ordermanage` DISABLE KEYS */;
INSERT INTO `ordermanage` VALUES (1,'간장게장','rlarlxo','1','완료','N','M100','2023-01-18'),(2,'간장게장','rlarlxo','1','완료','N','M100','2023-01-18'),(3,'해물찜','rlarlxo','1','완료','N','M200','2023-01-18'),(4,'해물찜','chlwlgur','3','완료','N','M200','2023-01-18'),(5,'해물찜','chlwlgur','1','완료','N','M200','2023-01-18'),(6,'해물찜','chlwlgur','1','완료','N','M200','2023-01-18'),(7,'해물찜','chlwlgur','1','완료','N','M200','2023-01-18'),(8,'해물찜','chlwlgur','1','완료','N','M200','2023-01-18'),(9,'해물찜','chlwlgur','1','완료','N','M200','2023-01-18'),(10,'해물찜','chlwlgur','1','완료','N','M200','2023-01-18'),(11,'해물찜','chlwlgur','3','완료','N','m200','2023-01-18'),(12,'해물찜','chlwlgur','3','완료','N','m200','2023-01-18'),(13,'오징어 초무침','chlwlgur','6','완료','N','m500','2023-01-18'),(14,'고등어조림','chlwlgur','8','완료','N','m300','2023-01-18'),(15,'고등어조림','chlwlgur','11','주문','N','m300','2023-01-18'),(16,'서대회','chlwlgur','10','주문','N','m400','2023-01-18'),(17,'간장게장','chlwlgur','10','주문','N','m100','2023-01-18'),(18,'고등어조림','chlwlgur','8','주문','N','m300','2023-01-18'),(19,'오징어 초무침','chlwlgur','9','주문','N','m500','2023-01-18'),(20,'고등어조림','chlwlgur','3','완료','N','m300','2023-01-18'),(21,'해물찜','chlwlgur','5','완료','N','m200','2023-01-18'),(22,'간장게장','chlwlgur','9','완료','N','m100','2023-01-18'),(23,'고등어조림','chlwlgur','9','완료','N','m300','2023-01-18'),(24,'고등어조림','chlwlgur','4','주문','N','m300','2023-01-18'),(25,'해물찜','chlwlgur','3','주문','N','m200','2023-01-18'),(26,'서대회','chlwlgur','10','주문','N','m400','2023-01-18'),(27,'서대회','chlwlgur','8','주문','N','m400','2023-01-18'),(28,'서대회','chlwlgur','4','주문','N','m400','2023-01-18'),(29,'고등어조림','chlwlgur','7','주문','N','m300','2023-01-18'),(297,'오징어 초무침','admin','7','완료','N','m500','2023-01-19'),(298,'오징어 초무침','admin','7','완료','N','m500','2023-01-19');
/*!40000 ALTER TABLE `ordermanage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_info` (
  `id` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `address` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES ('admin','aa','관리자','광인개'),('chlwlgur','aa','최지혁','광인개'),('rlarlxo','aa','김기태','광인개'),('wjdcjfdn','aa','정철우','광인개');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `max_menu`
--

/*!50001 DROP VIEW IF EXISTS `max_menu`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`wlgur`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `max_menu` AS select `a`.`메뉴코드` AS `메뉴코드`,`a`.`재료이름` AS `재료이름`,`a`.`수량` AS `수량`,`a`.`재료코드` AS `재료코드`,`b`.`남은수량` AS `남은수량`,(`b`.`남은수량` / `a`.`수량`) AS `최대개수` from (`bom` `a` join `inventory` `b` on((`a`.`재료코드` = `b`.`재료코드`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-19 16:32:18

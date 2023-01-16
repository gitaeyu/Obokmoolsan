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
  `단가` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bom`
--

LOCK TABLES `bom` WRITE;
/*!40000 ALTER TABLE `bom` DISABLE KEYS */;
INSERT INTO `bom` VALUES ('m100','간장게장','간장','c001','600','ml','1800'),('m100','간장게장','꽃게','c006','1','kg','10000'),('m100','간장게장','사과','c018','400','g','2000'),('m100','간장게장','생강가루','c020','15','ml','150'),('m100','간장게장','소주 ','c024','45','ml','270'),('m100','간장게장','청양고추','c031','40','g','320'),('m100','간장게장','통마늘','c034','500','g','5000'),('m100','간장게장','풋고추','c035','20','g','100'),('m200','해물찜','고춧가루','c004','90','g','2700'),('m200','해물찜','관자','c005','100','g','6000'),('m200','해물찜','다시마','c007','10','g','300'),('m200','해물찜','다진 마늘','c008','15','g','45'),('m200','해물찜','다진 생강','c009','5','g','150'),('m200','해물찜','다진 파','c010','30','g','90'),('m200','해물찜','멸치','c015','20','g','200'),('m200','해물찜','새우','c019','200','g','4800'),('m200','해물찜','설탕','c022','10','g','10'),('m200','해물찜','소금','c023','15','g','15'),('m200','해물찜','오징어','c028','180','g','1260'),('m200','해물찜','전분','c029','30','g','45'),('m200','해물찜','참기름','c030','10','ml','100'),('m200','해물찜','콩나물','c032','500','g','1500'),('m300','고등어조림','고등어','c002','2','팩','3000'),('m300','고등어조림','고추장','c003','15','g','30'),('m300','고등어조림','고춧가루','c004','30','g','900'),('m300','고등어조림','다진 마늘','c008','15','g','45'),('m300','고등어조림','대파','c012','20','g','100'),('m300','고등어조림','된장','c013','15','g','25.5'),('m300','고등어조림','맛술','c014','45','ml','225'),('m300','고등어조림','무','c016','200','g','300'),('m300','고등어조림','물엿','c017','15','ml','27'),('m300','고등어조림','설탕','c022','15','g','15'),('m300','고등어조림','양파','c026','300','g','450'),('m300','고등어조림','청양고추','c031','20','g','160'),('m400','서대회','고추장','c003','45','g','90'),('m400','서대회','고춧가루','c004','30','g','900'),('m400','서대회','다진 마늘','c008','15','g','45'),('m400','서대회','다진 생강','c009','5','g','150'),('m400','서대회','다진 파','c010','30','g','90'),('m400','서대회','대파','c012','20','g','100'),('m400','서대회','무','c016','100','g','150'),('m400','서대회','서대','c021','500','g','3000'),('m400','서대회','설탕','c022','30','g','30'),('m400','서대회','소금','c023','10','g','10'),('m400','서대회','식초','c025','45','ml','45'),('m400','서대회','청양고추','c031','10','g','80'),('m400','서대회','풋고추','c035','10','g','50'),('m500','오징어 초무침','간장','c001','50','ml','150'),('m500','오징어 초무침','고추장','c003','5','g','10'),('m500','오징어 초무침','고춧가루','c004','15','g','450'),('m500','오징어 초무침','다진 마늘','c008','5','g','15'),('m500','오징어 초무침','당근','c011','200','g','600'),('m500','오징어 초무침','설탕','c022','20','g','20'),('m500','오징어 초무침','식초','c025','20','ml','20'),('m500','오징어 초무침','양파','c026','600','g','900'),('m500','오징어 초무침','오이','c027','600','g','2400'),('m500','오징어 초무침','오징어','c028','180','g','1260'),('m500','오징어 초무침','참기름','c030','5','ml','50'),('m500','오징어 초무침','통깨','c033','10','g','85');
/*!40000 ALTER TABLE `bom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inquiry_manage`
--

DROP TABLE IF EXISTS `inquiry_manage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inquiry_manage` (
  `문의번호` varchar(45) NOT NULL,
  `주문번호` varchar(45) DEFAULT NULL,
  `제품명` varchar(45) DEFAULT NULL,
  `제품코드` varchar(45) DEFAULT NULL,
  `상태` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`문의번호`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inquiry_manage`
--

LOCK TABLES `inquiry_manage` WRITE;
/*!40000 ALTER TABLE `inquiry_manage` DISABLE KEYS */;
/*!40000 ALTER TABLE `inquiry_manage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `재료이름` varchar(45) DEFAULT NULL,
  `재료코드` varchar(45) DEFAULT NULL,
  `남은 수량` varchar(45) DEFAULT NULL,
  `단위` varchar(45) DEFAULT NULL,
  `기준수량` varchar(45) DEFAULT NULL,
  `가격` varchar(45) DEFAULT NULL,
  `단위가격` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('간장','c001','15000','ml','15000','45000','3'),('고등어','c002','40','팩','20','30000','1500'),('고추장','c003','14000','g','14000','28000','2'),('고춧가루','c004','2000','g','2000','60000','30'),('관자','c005','3000','g','100','6000','60'),('꽃게','c006','30','kg','3','30000','10000'),('다시마','c007','1000','g','200','6000','30'),('다진 마늘','c008','5000','g','1000','3000','3'),('다진 생강','c009','3000','g','300','9000','30'),('다진 파','c010','1000','g','1000','3000','3'),('당근','c011','5000','g','5000','15000','3'),('대파','c012','1000','g','1000','5000','5'),('된장','c013','14000','g','14000','23800','1.7'),('맛술','c014','1800','ml','1800','9000','5'),('멸치','c015','2000','g','2000','20000','10'),('무','c016','20000','g','20000','30000','1.5'),('물엿','c017','10000','g','10000','18000','1.8'),('사과','c018','10000','g','10000','50000','5'),('새우','c019','1000','g','1000','24000','24'),('생강가루','c020','1000','g','1000','10000','10'),('서대','c021','5000','g','500','3000','6'),('설탕','c022','15000','g','15000','15000','1'),('소금','c023','15000','g','15000','15000','1'),('소주','c024','7500','ml','375','2250','6'),('식초','c025','15000','ml','15000','15000','1'),('양파','c026','20000','g','20000','30000','1.5'),('오이','c027','10000','g','10000','40000','4'),('오징어','c028','20000','g','20000','140000','7'),('전분','c029','1000','g','1000','1500','1.5'),('참기름','c030','1800','ml','1800','18000','10'),('청양고추','c031','1000','g','1000','8000','8'),('콩나물','c032','10000','g','500','1500','3'),('통깨','c033','1000','g','1000','8500','8.5'),('통마늘','c034','1000','g','1000','10000','10'),('풋고추','c035','1000','g','1000','5000','5');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menulist`
--

DROP TABLE IF EXISTS `menulist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menulist` (
  `메뉴코드` varchar(45) DEFAULT NULL,
  `메뉴명` varchar(45) DEFAULT NULL,
  `가격` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menulist`
--

LOCK TABLES `menulist` WRITE;
/*!40000 ALTER TABLE `menulist` DISABLE KEYS */;
INSERT INTO `menulist` VALUES ('m001','간장게장','30000'),('m002','해물찜','30000'),('m003','고등어조림','12000'),('m004','서대회','9000'),('m005','오징어 초무침','12000');
/*!40000 ALTER TABLE `menulist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordermanage`
--

DROP TABLE IF EXISTS `ordermanage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordermanage` (
  `주문번호` varchar(45) NOT NULL,
  `메뉴명` varchar(45) DEFAULT NULL,
  `메뉴코드` varchar(45) DEFAULT NULL,
  `상태` varchar(45) DEFAULT NULL,
  `취소여부` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`주문번호`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordermanage`
--

LOCK TABLES `ordermanage` WRITE;
/*!40000 ALTER TABLE `ordermanage` DISABLE KEYS */;
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
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-16 21:10:35

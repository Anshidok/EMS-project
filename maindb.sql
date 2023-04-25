/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - main-project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`main-project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `main-project`;

/*Table structure for table `bookings` */

DROP TABLE IF EXISTS `bookings`;

CREATE TABLE `bookings` (
  `bkid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `venueid` int(11) DEFAULT NULL,
  `hid` int(11) DEFAULT NULL,
  `cname` varchar(30) DEFAULT NULL,
  `cphone` bigint(20) DEFAULT NULL,
  `caddress` varchar(30) DEFAULT NULL,
  `cemail` varchar(30) DEFAULT NULL,
  `cplace` varchar(30) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `curdate` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bkid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `bookings` */

insert  into `bookings`(`bkid`,`lid`,`venueid`,`hid`,`cname`,`cphone`,`caddress`,`cemail`,`cplace`,`date`,`status`,`curdate`) values 
(1,6,9,2,'sinan',999507575,NULL,'oksinan999@gmail.com','kavumpuram','03/31/2023','Pending',NULL),
(3,4,9,1,'Muhammed Anshid. OK',7034283888,'Oravakkottil (H),','anshid283@gmail.com','kavumpuram','04/02/2023','Aprove','2023-04-02'),
(4,8,9,1,'Muhammed',7034283888,'Oravakkottil (H),','anshid283@gmail.com','valancheryuuuuu','04/06/2023','Pending','2023-04-06'),
(5,4,9,1,'OK',7034283888,'Oravakkottil (H),','anshid283@gmail.com','valanchery','04/06/2023','Pending','2023-04-15'),
(6,9,9,1,'K',7034283888,'Oravakkottil (H),','anshid283@gmail.com','valancheryuuuuu','04/22/2023','Reject','2023-04-15');

/*Table structure for table `contact` */

DROP TABLE IF EXISTS `contact`;

CREATE TABLE `contact` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `subject` varchar(20) DEFAULT NULL,
  `message` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `contact` */

insert  into `contact`(`cid`,`lid`,`name`,`email`,`subject`,`message`) values 
(3,4,'anshid','auar070@gamil.com','testing','mail testing'),
(4,4,'anshid','anshid283@gmail.com','about mailssssssss','about mailssssssss');

/*Table structure for table `customize` */

DROP TABLE IF EXISTS `customize`;

CREATE TABLE `customize` (
  `czid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `eventid` int(11) DEFAULT NULL,
  `catering` varchar(20) DEFAULT NULL,
  `ac` varchar(20) DEFAULT NULL,
  `stage` varchar(20) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`czid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `customize` */

insert  into `customize`(`czid`,`lid`,`eventid`,`catering`,`ac`,`stage`,`count`,`time`) values 
(1,6,2,'Team','yes','yes',500,'3');

/*Table structure for table `datecheck` */

DROP TABLE IF EXISTS `datecheck`;

CREATE TABLE `datecheck` (
  `lid` int(11) DEFAULT NULL,
  `hid` int(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  KEY `hid` (`hid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `datecheck` */

insert  into `datecheck`(`lid`,`hid`,`date`) values 
(6,2,'03/31/2023'),
(4,1,'03/13/2023'),
(4,1,'03/29/2023'),
(4,1,''),
(4,1,''),
(4,1,'04/08/2023'),
(4,1,''),
(4,1,''),
(4,1,''),
(4,1,'03/27/2023');

/*Table structure for table `events` */

DROP TABLE IF EXISTS `events`;

CREATE TABLE `events` (
  `eventid` int(11) NOT NULL AUTO_INCREMENT,
  `eventtype` varchar(20) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`eventid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `events` */

insert  into `events`(`eventid`,`eventtype`,`description`,`image`) values 
(1,'Birthday party','Birthday party','20230222160438.jpg'),
(2,'Birthday ','dfdfdf','20230307195711.jpg');

/*Table structure for table `halls` */

DROP TABLE IF EXISTS `halls`;

CREATE TABLE `halls` (
  `hid` int(11) NOT NULL AUTO_INCREMENT,
  `addid` int(11) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `bprice` int(10) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `descri` varchar(50) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`hid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `halls` */

insert  into `halls`(`hid`,`addid`,`location`,`name`,`bprice`,`phone`,`email`,`descri`,`image`) values 
(1,9,'Kavumpuram','Parakkal Convention center',33000,1234567890,'parakkalconvention@gmail.com','best convention Centre in valanchery, kavumpuram','20230401102709.jpg'),
(2,1,'Tirur','Bianco Castle',60000,1234567890,'biancocastle@gamil.com','top premium center in tirur','20230405060643.jpg');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(4,'anshid','123','user'),
(6,'jasi','123','user'),
(8,'anshi','111','user'),
(9,'vn1','1234','venue');

/*Table structure for table `payconfirm` */

DROP TABLE IF EXISTS `payconfirm`;

CREATE TABLE `payconfirm` (
  `bkid` int(11) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `phone` int(20) DEFAULT NULL,
  `addid` int(11) DEFAULT NULL,
  `upiref` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payconfirm` */

insert  into `payconfirm`(`bkid`,`lid`,`name`,`phone`,`addid`,`upiref`) values 
(3,4,'Muhammed Anshid. OK',2147483647,9,'123456789000'),
(3,4,'Muhammed Anshid. OK',2147483647,9,'123456789000');

/*Table structure for table `paymentd` */

DROP TABLE IF EXISTS `paymentd`;

CREATE TABLE `paymentd` (
  `lid` int(11) DEFAULT NULL,
  `hid` int(11) DEFAULT NULL,
  `upid` varchar(50) DEFAULT NULL,
  `qrcode` varchar(50) DEFAULT NULL,
  `advance` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `paymentd` */

insert  into `paymentd`(`lid`,`hid`,`upid`,`qrcode`,`advance`) values 
(9,1,'parakkal@okhdfcbank','20230420171044.jpg',NULL);

/*Table structure for table `signup` */

DROP TABLE IF EXISTS `signup`;

CREATE TABLE `signup` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `signup` */

insert  into `signup`(`uid`,`lid`,`name`,`phone`,`email`) values 
(3,4,'anshid',7034283888,'email@gmail.com'),
(5,6,'jasi',7034283888,'email@gmail.com'),
(7,8,'anshid',7034283888,'283@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

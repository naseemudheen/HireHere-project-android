/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - part_time_job
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`part_time_job` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `part_time_job`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(1000) NOT NULL,
  `name` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

/*Table structure for table `employer` */

DROP TABLE IF EXISTS `employer`;

CREATE TABLE `employer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `post` varchar(25) NOT NULL,
  `pin` int(11) NOT NULL,
  `contact` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `employer` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(1000) NOT NULL,
  `name` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `job` */

DROP TABLE IF EXISTS `job`;

CREATE TABLE `job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job` varchar(20) NOT NULL,
  `company` varchar(30) NOT NULL,
  `salary` int(11) NOT NULL,
  `place` varchar(20) NOT NULL,
  `contact_no` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `job` */

/*Table structure for table `jobseeker` */

DROP TABLE IF EXISTS `jobseeker`;

CREATE TABLE `jobseeker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` int(11) NOT NULL,
  `phoneno` int(10) NOT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `jobseeker` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(10) NOT NULL,
  `type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'admin','password12','admin');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

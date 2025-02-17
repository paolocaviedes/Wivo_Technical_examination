-- MySQL Script generated by MySQL Workbench
-- 08/03/17 18:16:18
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema wivo
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `wivo` ;

-- -----------------------------------------------------
-- Schema wivo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `wivo` DEFAULT CHARACTER SET utf8 ;
USE `wivo` ;

-- -----------------------------------------------------
-- Table `wivo`.`events`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wivo`.`events` ;

CREATE TABLE IF NOT EXISTS `wivo`.`events` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `object_name` VARCHAR(150) NOT NULL,
  `event` VARCHAR(45) NOT NULL,
  `value` VARCHAR(45) NOT NULL,
  `metric_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `wivo`.`file_registry`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wivo`.`file_registry` ;

CREATE TABLE IF NOT EXISTS `wivo`.`file_registry` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `extension` VARCHAR(45) NOT NULL,
  `created` DATETIME NOT NULL,
  `edited` DATETIME NOT NULL,
  `directorio` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `wivo`.`function`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wivo`.`function` ;

CREATE TABLE IF NOT EXISTS `wivo`.`function` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `parameters` JSON NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `wivo`.`metric`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wivo`.`metric` ;

CREATE TABLE IF NOT EXISTS `wivo`.`metric` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `unit` VARCHAR(45) NOT NULL,
  `representation` VARCHAR(45) NOT NULL,
  `derived_form` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `indx_name` (`name` ASC),
  INDEX `indx_derived_form` (`derived_form` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `wivo`.`object`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wivo`.`object` ;

CREATE TABLE IF NOT EXISTS `wivo`.`object` (
  `id` INT(11) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `external_reference` VARCHAR(45) NOT NULL,
  `metadata` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `indx_name` (`name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

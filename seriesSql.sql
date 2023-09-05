
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema seriesdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema seriesdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `seriesdb` DEFAULT CHARACTER SET utf8 ;
USE `seriesdb` ;

-- -----------------------------------------------------
-- Table `seriesdb`.`series`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seriesdb`.`series` (
  `ID_serie` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `total_seasons` INT NOT NULL,
  `total_episodes` INT NOT NULL,
  `last_seen_season` INT NULL,
  `last_seen_episode` INT NULL,
  PRIMARY KEY (`ID_serie`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `seriesdb`.`seasons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seriesdb`.`seasons` (
  `ID_season` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `total_episodes` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`ID_season`),
  FOREIGN KEY (`ID_season`) REFERENCES `seriesdb`.`series` (`ID_serie`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


SELECT * FROM series;































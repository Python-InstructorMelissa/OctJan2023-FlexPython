-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema week13Baseball
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `week13Baseball` ;

-- -----------------------------------------------------
-- Schema week13Baseball
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `week13Baseball` DEFAULT CHARACTER SET utf8 ;
USE `week13Baseball` ;

-- -----------------------------------------------------
-- Table `week13Baseball`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `week13Baseball`.`user` ;

CREATE TABLE IF NOT EXISTS `week13Baseball`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `week13Baseball`.`game`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `week13Baseball`.`game` ;

CREATE TABLE IF NOT EXISTS `week13Baseball`.`game` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `team1` VARCHAR(255) NULL,
  `team2` VARCHAR(255) NULL,
  `final_score` VARCHAR(255) NULL,
  `game_info` TEXT NULL,
  `game_date` DATE NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_game_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_game_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `week13Baseball`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `week13Baseball`.`watch`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `week13Baseball`.`watch` ;

CREATE TABLE IF NOT EXISTS `week13Baseball`.`watch` (
  `user_id` INT NOT NULL,
  `game_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `game_id`),
  INDEX `fk_user_has_game_game1_idx` (`game_id` ASC) VISIBLE,
  INDEX `fk_user_has_game_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_game_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `week13Baseball`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_user_has_game_game1`
    FOREIGN KEY (`game_id`)
    REFERENCES `week13Baseball`.`game` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

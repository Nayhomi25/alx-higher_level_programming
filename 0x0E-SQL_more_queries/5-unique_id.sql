-- creates the table unique_id
-- id INT with the default value 1, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS `unique_id` (`id` INT DEFAULT 1 UNIQUE, `name` VARCHAR(256));

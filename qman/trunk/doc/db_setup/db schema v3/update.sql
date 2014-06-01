-- add opening hours for each week day

ALTER TABLE `queues_details` DROP COLUMN `opening_hour_local_timezone`;
ALTER TABLE `queues_details` DROP COLUMN `opening_minute_local_timezone`;
ALTER TABLE `queues_details` DROP COLUMN `closing_hour_local_timezone`;
ALTER TABLE `queues_details` DROP COLUMN `closing_minute_local_timezone`;
ALTER TABLE `queues_details` DROP COLUMN `opening_hour_utc`;
ALTER TABLE `queues_details` DROP COLUMN `opening_minute_utc`;
ALTER TABLE `queues_details` DROP COLUMN `closing_hour_utc`;
ALTER TABLE `queues_details` DROP COLUMN `closing_minute_utc`;

CREATE TABLE `queues_opening_hours` (
  `queue_id` int(10) unsigned NOT NULL,
  `day_id` int(10) unsigned NOT NULL,
  `opening_hour_local_timezone` tinyint(2) unsigned NOT NULL,
  `opening_minute_local_timezone` tinyint(2) unsigned NOT NULL,
  `closing_hour_local_timezone` tinyint(2) unsigned NOT NULL,
  `closing_minute_local_timezone` tinyint(2) unsigned NOT NULL,
  `opening_hour_utc` tinyint(2) unsigned NOT NULL,
  `opening_minute_utc` tinyint(2) unsigned NOT NULL,
  `closing_hour_utc` tinyint(2) unsigned NOT NULL,
  `closing_minute_utc` tinyint(2) unsigned NOT NULL,
  PRIMARY KEY (`queue_id`, `day_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(1, 2, 9, 30, 17, 30, 8, 30, 16, 30);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(1, 3, 9, 30, 17, 30, 8, 30, 16, 30);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(1, 4, 9, 30, 17, 30, 8, 30, 16, 30);
	
INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(1, 5, 9, 30, 17, 30, 8, 30, 16, 30);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(1, 6, 9, 30, 17, 30, 8, 30, 16, 30);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(2, 2, 9, 30, 17, 30, 8, 30, 16, 30);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(2, 3, 9, 30, 17, 30, 8, 30, 16, 30);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(2, 4, 9, 30, 17, 30, 8, 30, 16, 30);
	
INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(2, 5, 9, 30, 17, 30, 8, 30, 16, 30);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(2, 6, 9, 30, 17, 30, 8, 30, 16, 30);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(3, 2, 17, 30, 23, 59, 16, 30, 22, 59);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(3, 3, 17, 30, 23, 59, 16, 30, 22, 59);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(3, 4, 17, 30, 23, 59, 16, 30, 22, 59);
	
INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(3, 5, 17, 30, 23, 59, 16, 30, 22, 59);

INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(3, 6, 17, 30, 23, 59, 16, 30, 22, 59);
	
INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(3, 7, 17, 30, 23, 59, 16, 30, 22, 59);
	
INSERT INTO `queues_opening_hours` 
	(`queue_id`,
	`day_id`,
	`opening_hour_local_timezone`, 
	`opening_minute_local_timezone`,
	`closing_hour_local_timezone`, 
	`closing_minute_local_timezone`,
	`opening_hour_utc`, 
	`opening_minute_utc`, 
	`closing_hour_utc`, 
	`closing_minute_utc`) 
VALUES 
	(3, 1, 17, 30, 23, 59, 16, 30, 22, 59);
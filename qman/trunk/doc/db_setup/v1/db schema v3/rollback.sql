-- add opening hours for each week day

ALTER TABLE `queues_details` ADD `queue_id` int(10) unsigned NOT NULL;
ALTER TABLE `queues_details` ADD `day_id` int(10) unsigned NOT NULL;
ALTER TABLE `queues_details` ADD `opening_hour_local_timezone` tinyint(2) unsigned NOT NULL;
ALTER TABLE `queues_details` ADD `opening_minute_local_timezone` tinyint(2) unsigned NOT NULL;
ALTER TABLE `queues_details` ADD `closing_hour_local_timezone` tinyint(2) unsigned NOT NULL;
ALTER TABLE `queues_details` ADD `closing_minute_local_timezone` tinyint(2) unsigned NOT NULL;
ALTER TABLE `queues_details` ADD `opening_hour_utc` tinyint(2) unsigned NOT NULL;
ALTER TABLE `queues_details` ADD `opening_minute_utc` tinyint(2) unsigned NOT NULL;
ALTER TABLE `queues_details` ADD `closing_hour_utc` tinyint(2) unsigned NOT NULL;
ALTER TABLE `queues_details` ADD `closing_minute_utc` tinyint(2) unsigned NOT NULL;

UPDATE `queues_details` SET 
	`opening_hour_local_timezone` = 9,
	`opening_minute_local_timezone` = 30, 
	`closing_hour_local_timezone` = 17, 
	`closing_minute_local_timezone` = 30,
	`opening_hour_utc` = 8, 
	`opening_minute_utc` = 30, 
	`closing_hour_utc` = 16, 
	`closing_minute_utc` = 30
WHERE queue_id IN (1,2);

UPDATE `queues_details` SET 
	`opening_hour_local_timezone` = 17,
	`opening_minute_local_timezone` = 30, 
	`closing_hour_local_timezone` = 23, 
	`closing_minute_local_timezone` = 59,
	`opening_hour_utc` = 16, 
	`opening_minute_utc` = 30, 
	`closing_hour_utc` = 22, 
	`closing_minute_utc` = 59
WHERE queue_id = 3;

DROP TABLE `queues_opening_hours`;
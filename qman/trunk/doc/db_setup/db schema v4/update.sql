insert into queues (`queue_id`, `name`) values (4,'PPS');

INSERT INTO `queues_details`
(`queue_id`,
`latitude`, `longitude`,
`phone_number`,
`address_line_1`, `address_line_2`,
`town_city`, `county`, `post_code`, `country`, `email`, `default_average_waiting_time`, `description`)
values
(4,
53.350683, -6.266074,
"0035318899500",
"197/199 Parnell Street", "",
"Dublin", "Dublin", "D1", "Republic of Ireland", "", 18000,
"Personal Public Service Number (PPS Number) is a unique reference number that helps you access social welfare benefits, public services and information in Ireland. State agencies that use PPS Numbers to identify individuals include the Department of Social Protection, the Revenue Commissioners and the Health Service Executive (HSE).");

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
	(4, 2, 9, 30, 16, 00, 8, 30, 15, 00);
	
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
	(4, 3, 9, 30, 16, 00, 8, 30, 15, 00);
	
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
	(4, 4, 9, 30, 16, 00, 8, 30, 15, 00);

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
	(4, 5, 10, 30, 16, 00, 9, 30, 15, 00);
	
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
	(4, 6, 9, 30, 16, 00, 8, 30, 15, 00);
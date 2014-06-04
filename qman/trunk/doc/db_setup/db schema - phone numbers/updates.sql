CREATE TABLE `queues_phone_numbers` (
  `queue_id` int(10) unsigned NOT NULL,
  `phone_country_code` varchar(10),
  `phone_area_code` varchar(10),
  `phone_line_number` varchar(15),
  `phone_extension` varchar(10),
  PRIMARY KEY (`queue_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO  `queues_phone_numbers` 
(queue_id, phone_country_code, phone_area_code, phone_line_number, phone_extension)
VALUES
(1, '353', '1', '6669100', '');

INSERT INTO  `queues_phone_numbers` 
(queue_id, phone_country_code, phone_area_code, phone_line_number, phone_extension)
VALUES
(2, '', '1890', '551500', '');

INSERT INTO  `queues_phone_numbers` 
(queue_id, phone_country_code, phone_area_code, phone_line_number, phone_extension)
VALUES
(3, '48', '22', '4430000', '');

INSERT INTO  `queues_phone_numbers` 
(queue_id, phone_country_code, phone_area_code, phone_line_number, phone_extension)
VALUES
(4, '353', '1', '8899500', '');

ALTER TABLE `queues_details` DROP COLUMN `phone_number`;
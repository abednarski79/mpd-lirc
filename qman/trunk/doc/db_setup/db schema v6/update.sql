update queues_opening_hours set day_id = 1 where day_id = 6 and queue_id in (1, 2);
update queues_opening_hours set day_id = 1 where day_id = 4 and queue_id = 4;
update queues_opening_hours set day_id = 4 where day_id = 5 and queue_id = 4;
update queues_opening_hours set day_id = 5 where day_id = 6 and queue_id = 4;

ALTER TABLE `queues_details` ADD COLUMN `phone_country_code` varchar(5);
ALTER TABLE `queues_details` ADD COLUMN `phone_area_code_and_local_number` varchar(20);
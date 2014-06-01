ALTER TABLE `queues_details` ADD COLUMN `website` varchar(2048);
ALTER TABLE `queues_details` ADD COLUMN `name` varchar(200);

UPDATE `queues_details` set website = 'http://www.garda.ie' where queue_id = 1;
UPDATE `queues_details` set website = 'http://www.inis.gov.ie' where queue_id = 2;
UPDATE `queues_details` set website = 'http://www.um.warszawa.pl/' where queue_id = 3;
UPDATE `queues_details` set website = 'http://www.welfare.ie/en/Pages/office/intreocentreparnellstreet.aspx' where queue_id = 4;

UPDATE `queues_details` set name = 'Garda National Immigration Bureau' where queue_id = 1;
UPDATE `queues_details` set name = 'Irish Naturalisation and Immigration Service' where queue_id = 2;
UPDATE `queues_details` set name = 'Urząd Miasta Stołecznego Warszawy' where queue_id = 3;
UPDATE `queues_details` set name = 'Intreo Centre Parnell Street' where queue_id = 4; 

UPDATE `queues_details` set phone_number = '0035316669100' where queue_id = 1;
UPDATE `queues_details` set phone_number = '1890551500' where queue_id = 2;
UPDATE `queues_details` set phone_number = '0048224430000' where queue_id = 3;
UPDATE `queues_details` set phone_number = '0035318899500' where queue_id = 4;


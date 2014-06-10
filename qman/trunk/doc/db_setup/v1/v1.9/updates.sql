--Monday 8am - 9pm
--Tuesday 8am - 9pm
--Wednesday 8am - 9pm
--Thursday 8am - 9pm
update queues_opening_hours
set
opening_hour_local_timezone = 8,
opening_minute_local_timezone = 0,
closing_hour_local_timezone = 21, 
closing_minute_local_timezone = 0,
opening_hour_utc = 7, 
opening_minute_utc = 0, 
closing_hour_utc = 20, 
closing_minute_utc = 0
where
queue_id in (1, 2) and day_id in (1, 2, 3, 4); 

--Friday 8am - 6pm
update queues_opening_hours
set
opening_hour_local_timezone = 8,
opening_minute_local_timezone = 0,
closing_hour_local_timezone = 18, 
closing_minute_local_timezone = 0,
opening_hour_utc = 7, 
opening_minute_utc = 0, 
closing_hour_utc = 17, 
closing_minute_utc = 0
where
queue_id in (1, 2) and day_id = 5; 
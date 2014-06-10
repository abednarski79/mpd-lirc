CREATE TABLE `feedbacks` (
  `feedback_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `rating` int(1),
  `comment` varchar(1000),
  `queue_id` int(10) unsigned,
  `created` datetime NOT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



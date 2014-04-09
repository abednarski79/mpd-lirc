package eu.appbucket.queue.persistence;

import org.springframework.stereotype.Repository;

import eu.appbucket.queue.domain.ticket.TicketUpdate;

@Repository
public class TicketDaoImpl implements TicketDao {
/*CREATE TABLE `updates` (
  `update_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `queue_id` int(10) unsigned NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_ticket` int(10) unsigned NOT NULL,
  `served_ticket` int(10) unsigned NOT NULL,
  `valid` binary(1) NOT NULL,
  PRIMARY KEY (`update_id`),
FOREIGN KEY (`queue_id`)
REFERENCES `queues`(`queue_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;*/
	
	private final static String SQL_INSERT_TICKET_UPDATE = "SELECT * FROM queues";
	
	public void storeTicketUpdate(TicketUpdate ticketUpdate) {
		// TODO Auto-generated method stub
		
	}

}

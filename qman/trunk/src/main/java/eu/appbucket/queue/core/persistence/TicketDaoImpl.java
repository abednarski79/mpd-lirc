package eu.appbucket.queue.core.persistence;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.simple.SimpleJdbcTemplate;
import org.springframework.stereotype.Repository;

import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

@Repository
public class TicketDaoImpl implements TicketDao {
	
	private final static String SQL_INSERT_TICKET_UPDATE = 
			"INSERT INTO updates(`queue_id`, `user_ticket`, `served_ticket`, `is_valid`) "
			+ "VALUES (?, ?, ?, 1)";
	
	private SimpleJdbcTemplate jdbcTempalte;
	
	@Autowired
	public void setJdbcTempalte(SimpleJdbcTemplate jdbcTempalte) {
		this.jdbcTempalte = jdbcTempalte;
	}
	
	public void storeTicketUpdate(TicketUpdate ticketUpdate) {
		jdbcTempalte.update(SQL_INSERT_TICKET_UPDATE, 
				ticketUpdate.getQueueInfo().getQueueId(),
				ticketUpdate.getClientTicketNumber(),
				ticketUpdate.getCurrentlyServicedTicketNumber());		
	}

}

package eu.appbucket.queue.core.persistence;

import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

public interface TicketDao {
	public void storeTicketUpdate(TicketUpdate ticketUpdate);

}

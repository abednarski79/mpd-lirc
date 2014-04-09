package eu.appbucket.queue.persistence;

import eu.appbucket.queue.domain.ticket.TicketUpdate;

public interface TicketDao {
	public void storeTicketUpdate(TicketUpdate ticketUpdate);
}

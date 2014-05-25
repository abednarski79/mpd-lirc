package eu.appbucket.queue.core.persistence;

import java.util.Collection;
import java.util.Date;

import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

public interface TicketDao {
	
	// clean: ticketUpdatesCache, highestTicketUpdateCache
	public void storeTicketUpdate(TicketUpdate ticketUpdate);
	
	// ticketUpdatesCache
	public Collection<TicketUpdate> readTicketUpdatesByQueueAndDate(
			QueueInfo queueInfo, 
			Date fromDate, Date toDate, 
			int minAcceptedInputQuality);
	
	// highestTicketUpdateCache
	public TicketUpdate readHighestTicketUpdateByQueueAndDay(
			QueueInfo queueInfo, 
			Date fromDate, Date toDate, 
			int minAcceptedInputQuality);
}

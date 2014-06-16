package eu.appbucket.queue.core.persistence;

import java.util.Collection;
import java.util.Date;

import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

public interface TicketDao {
		
	public void storeTicketUpdate(TicketUpdate ticketUpdate);
		
	public Collection<TicketUpdate> readTicketUpdatesByQueueAndDate(
			QueueInfo queueInfo, 
			Date fromDate, Date toDate, 
			int minAcceptedInputQuality);
	
	public TicketUpdate readHighestTicketUpdateByQueueAndDay(
			QueueInfo queueInfo, 
			Date fromDate, Date toDate, 
			int minAcceptedInputQuality);
	
	public void cleanHighestTicketUpdateByQueueAndDayCache(QueueInfo queueInfo);
}

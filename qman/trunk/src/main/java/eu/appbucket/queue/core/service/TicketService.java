package eu.appbucket.queue.core.service;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

public interface TicketService {
	
	TicketEstimation getTicketEstimation(QueueDetails queueDetails, QueueStats queueStats, int ticketId);
	void processTicketInformation(TicketUpdate ticketUpdate);
	TicketUpdate getHighestTicketUpdatesFromToday(QueueInfo queueInfo);
	
}

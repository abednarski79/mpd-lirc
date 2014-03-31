package eu.appbucket.queue.service;

import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueStats;
import eu.appbucket.queue.domain.ticket.TicketStats;
import eu.appbucket.queue.domain.ticket.TicketUpdate;

public interface TicketService {
	TicketStats getTicketStatistics(QueueDetails queueDetails, QueueStats queueStats, int ticketId);
	void updateTicketInformation(TicketUpdate ticketUpdate);
}

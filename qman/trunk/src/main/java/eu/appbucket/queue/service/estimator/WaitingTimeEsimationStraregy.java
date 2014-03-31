package eu.appbucket.queue.service.estimator;

import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueStats;
import eu.appbucket.queue.domain.ticket.TicketStats;

public interface WaitingTimeEsimationStraregy {	
	TicketStats estimateWaitingTime(QueueDetails queueDetails, QueueStats queueStats, int ticketNumber);
}

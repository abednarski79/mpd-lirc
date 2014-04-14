package eu.appbucket.queue.core.service.estimator;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;

public interface WaitingTimeEsimationStraregy {	
	TicketEstimation estimateWaitingTime(QueueDetails queueDetails, QueueStats queueStats, int ticketNumber);
}

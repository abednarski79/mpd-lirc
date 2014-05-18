package eu.appbucket.queue.core.service.estimator.duration;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;

public interface WaitingTimeEsimationStrategy {	
	TicketEstimation estimateTimeToBeServiced(QueueDetails queueDetails, QueueStats queueStats, int ticketNumber);
}

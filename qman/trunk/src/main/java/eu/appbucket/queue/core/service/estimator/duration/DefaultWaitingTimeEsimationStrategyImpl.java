package eu.appbucket.queue.core.service.estimator.duration;

import org.springframework.stereotype.Component;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;

/**
 * This default strategy calculated waiting time based on the client ticket number, current time 
 * and default average service duration in the queue.
 * This strategy is used when there is not enough queue updates available to make correct
 * estimation.
 */
@Component("defaultWaitingTimeEsimationStrategy")
public class DefaultWaitingTimeEsimationStrategyImpl implements WaitingTimeEsimationStrategy {
	
	public TicketEstimation estimateTimeToBeServiced(QueueDetails queueDetails, QueueStats queueStats, int ticketNumber) {
		long ticketTimeToBeServiced = 
				(queueDetails.getDefaultAverageWaitingDuration() * (ticketNumber - 1)) 
				+ queueDetails.getTodayOpeningTimesUTC().getOpeningTime();		
		TicketEstimation ticketStatus = new TicketEstimation();
		ticketStatus.setTimeToBeServiced(ticketTimeToBeServiced);
		return ticketStatus;
	}
}

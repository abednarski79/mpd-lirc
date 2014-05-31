package eu.appbucket.queue.core.service.estimator.duration;

import org.springframework.stereotype.Component;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;

/**
 * This strategy calculating waiting time based on the client ticket number, current time 
 * and calculated average waiting duration in the queue.
 * This strategy is used when there is enough (@see TicketServiceImpl) results to make
 * proper calculations.
 */
@Component("calculatedWaitingTimeEsimationStrategy")
public class CalculatedWaitingTimeEsimationStrategyImpl implements WaitingTimeEsimationStrategy {
	
	public TicketEstimation estimateTimeToBeServiced(QueueDetails queueDetails, QueueStats queueStats, int ticketNumber) {
		long ticketTimeToBeServiced = 
				(queueStats.getCalculatedAverageWaitingDuration() * (ticketNumber - 1)) 
				+ queueDetails.getTodayOpeningTimesUTC().getOpeningTime();		
		TicketEstimation ticketStatus = new TicketEstimation();
		ticketStatus.setTimeToBeServiced(ticketTimeToBeServiced);
		return ticketStatus;
	}
}

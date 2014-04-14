package eu.appbucket.queue.core.service.estimator;

import java.util.Calendar;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;

/**
 * This basic strategy calculated waiting time based on the client ticket number, current time and maximum number
 * of tickets given daily in the queue.
 *
 */
public class BasicWaitingTimeEsimationStraregyImpl implements WaitingTimeEsimationStraregy {
	
	public TicketEstimation estimateWaitingTime(QueueDetails queueDetails, QueueStats queueStats, int ticketNumber) {
		long ticketServiceTime = (queueStats.getAverageWaitingTime() * (ticketNumber - 1)) 
				+ queueDetails.getOpeningTimes().getOpeningTime();		
		TicketEstimation ticketStatus = new TicketEstimation();
		ticketStatus.setServiceTime(ticketServiceTime);
		return ticketStatus;
	}
}

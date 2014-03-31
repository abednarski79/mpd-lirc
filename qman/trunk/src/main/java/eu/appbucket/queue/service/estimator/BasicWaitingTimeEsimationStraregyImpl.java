package eu.appbucket.queue.service.estimator;

import java.util.Calendar;

import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueStats;
import eu.appbucket.queue.domain.ticket.TicketStats;

/**
 * This basic strategy calculated waiting time based on the client ticket number, current time and maximum number
 * of tickets given daily in the queue.
 *
 */
public class BasicWaitingTimeEsimationStraregyImpl implements WaitingTimeEsimationStraregy {
	
	public TicketStats estimateWaitingTime(QueueDetails queueDetails, QueueStats queueStats, int ticketNumber) {
		long ticketServiceTime = (queueStats.getAverageWaitingTime() * (ticketNumber - 1)) 
				+ queueDetails.getOpeningTimes().getOpeningTime();		
		TicketStats ticketStatus = new TicketStats();
		ticketStatus.setServiceTime(ticketServiceTime);
		return ticketStatus;
	}
}

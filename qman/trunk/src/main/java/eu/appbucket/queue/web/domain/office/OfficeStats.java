package eu.appbucket.queue.web.domain.office;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

public class OfficeStats {
	
	private Integer calculatedAverageWaitingTime;	
	private Integer defaultAverageWaitingTime;
	private Integer currentTicketNumber;
	
	public Integer getCalculatedAverageWaitingTime() {
		return calculatedAverageWaitingTime;
	}

	public void setCalculatedAverageWaitingTime(Integer calcualtedAverageWaitingTime) {
		this.calculatedAverageWaitingTime = calcualtedAverageWaitingTime;
	}
	
	public Integer getDefaultAverageWaitingTime() {
		return defaultAverageWaitingTime;
	}

	public void setDefaultAverageWaitingTime(Integer defaultAverageWaitingTime) {
		this.defaultAverageWaitingTime = defaultAverageWaitingTime;
	}

	public Integer getCurrentTicketNumber() {
		return currentTicketNumber;
	}

	public void setCurrentTicketNumber(Integer currentTicketNumber) {
		this.currentTicketNumber = currentTicketNumber;
	}

	public static OfficeStats fromQueueAndTicketData(QueueDetails queueDetails, 
			QueueStats queueStats, TicketUpdate ticketUpdate) {
		OfficeStats stats = new OfficeStats();
		stats.setCalculatedAverageWaitingTime(queueStats.getCalculatedAverageWaitingDuration());		
		stats.setDefaultAverageWaitingTime(queueDetails.getDefaultAverageWaitingDuration());
		if(ticketUpdate.getCurrentlyServicedTicketNumber() != 0) {
			stats.setCurrentTicketNumber(ticketUpdate.getCurrentlyServicedTicketNumber());
		}
		return stats;
	}
}

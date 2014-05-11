package eu.appbucket.queue.web.domain.ticket;

import eu.appbucket.queue.core.domain.ticket.TicketEstimation;

public class TicketStatus {	
		
	private long waitingTime;

	public long getWaitingTime() {
		return waitingTime;
	}

	public void setWaitingTime(long waitingTime) {
		this.waitingTime = waitingTime;
	}
	
	public static TicketStatus fromTicketEstimation(TicketEstimation ticketEstimation) {
		TicketStatus ticketStatus = new TicketStatus();
		ticketStatus.setWaitingTime(ticketEstimation.getTimeToBeServiced());		
		return ticketStatus;
	}
}

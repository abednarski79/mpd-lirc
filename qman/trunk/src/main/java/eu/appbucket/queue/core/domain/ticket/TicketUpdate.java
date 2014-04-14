package eu.appbucket.queue.core.domain.ticket;

import eu.appbucket.queue.core.domain.queue.QueueInfo;

public class TicketUpdate {	
	
	private int currentlyServicedTicketNumber;
	private int clientTicketNumber;
	private QueueInfo queueInfo;
	
	public int getCurrentlyServicedTicketNumber() {
		return currentlyServicedTicketNumber;
	}
	public void setCurrentlyServicedTicketNumber(int currentlyServicedTicketNumber) {
		this.currentlyServicedTicketNumber = currentlyServicedTicketNumber;
	}
	public QueueInfo getQueueInfo() {
		return queueInfo;
	}
	public void setQueueInfo(QueueInfo queueInfo) {
		this.queueInfo = queueInfo;
	}
	public int getClientTicketNumber() {
		return clientTicketNumber;
	}
	public void setClientTicketNumber(int clientTicketNumber) {
		this.clientTicketNumber = clientTicketNumber;
	}	
}

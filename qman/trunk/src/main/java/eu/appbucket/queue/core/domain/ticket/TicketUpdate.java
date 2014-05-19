package eu.appbucket.queue.core.domain.ticket;

import java.util.Date;

import eu.appbucket.queue.core.domain.queue.QueueInfo;

public class TicketUpdate {	
	
	private int currentlyServicedTicketNumber;
	private int clientTicketNumber;
	private QueueInfo queueInfo;
	private Date created;
	private int quality;
	
	public int getQuality() {
		return quality;
	}
	public void setQuality(int quality) {
		this.quality = quality;
	}
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
	public Date getCreated() {
		return created;
	}
	public void setCreated(Date created) {
		this.created = created;
	}
}

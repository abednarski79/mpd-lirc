package eu.appbucket.queue.core.domain.ticket;

import java.util.Date;

import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.web.domain.ticket.TicketInput;

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
	
	public static TicketUpdate fromTicketInputAndQueueInfo(int ticketNumber, TicketInput ticketInput, QueueInfo queueInfo) {
		TicketUpdate ticketUpdate = new TicketUpdate();
		ticketUpdate.setClientTicketNumber(ticketNumber);
		ticketUpdate.setCurrentlyServicedTicketNumber(ticketInput.getServicedTicketNumber());
		ticketUpdate.setQueueInfo(queueInfo);
		ticketUpdate.setCreated(new Date());
		return ticketUpdate;
	}
}

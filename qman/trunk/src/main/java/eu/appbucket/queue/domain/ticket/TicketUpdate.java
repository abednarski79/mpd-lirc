package eu.appbucket.queue.domain.ticket;

public class TicketUpdate {	
	
	private int currentlyServicedTicketNumber;
	

	public int getCurrentlyServicedTicketNumber() {
		return currentlyServicedTicketNumber;
	}


	public void setCurrentlyServicedTicketNumber(int currentlyServicedTicketNumber) {
		this.currentlyServicedTicketNumber = currentlyServicedTicketNumber;
	}


	@Override
	public String toString() {
		return "TicketUpdate [currentlyServicedTicketNumber=" + currentlyServicedTicketNumber + "]";
	}
}

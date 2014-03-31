package eu.appbucket.queue.domain.ticket;

import eu.appbucket.queue.domain.queue.GeographicalLocation;

public class TicketUpdate {	
	
	private int currentlyServicedTicketNumber;
	private GeographicalLocation location;	

	public int getCurrentlyServicedTicketNumber() {
		return currentlyServicedTicketNumber;
	}


	public void setCurrentlyServicedTicketNumber(int currentlyServicedTicketNumber) {
		this.currentlyServicedTicketNumber = currentlyServicedTicketNumber;
	}

	public GeographicalLocation getLocation() {
		return location;
	}

	public void setLocation(GeographicalLocation location) {
		this.location = location;
	}


	@Override
	public String toString() {
		return "TicketUpdate [currentlyServicedTicketNumber="
				+ currentlyServicedTicketNumber + ", location=" + location
				+ "]";
	}
}

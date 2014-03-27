package eu.appbucket.queue.domain.ticket;

public class TicketStatus {	
	
	private int waitingTimeInSeconds;
	
	public int getWaitingTimeInSeconds() {
		return waitingTimeInSeconds;
	}
	public void setWaitingTimeInSeconds(int waitingTimeInSeconds) {
		this.waitingTimeInSeconds = waitingTimeInSeconds;
	}
	
	@Override
	public String toString() {
		return "TicketStatus [waitingTimeInSeconds=" + waitingTimeInSeconds + "]";
	}
}

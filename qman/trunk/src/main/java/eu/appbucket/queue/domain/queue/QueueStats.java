package eu.appbucket.queue.domain.queue;

/**
 * Dynamically calculated information about queue.
 */
public class QueueStats {

	private int highestGivenTicketNumber;
	private long averageWaitingTime;
	
	public int getHighestGivenTicketNumber() {
		return highestGivenTicketNumber;
	}

	public void setHighestGivenTicketNumber(int highestGivenTicketNumber) {
		this.highestGivenTicketNumber = highestGivenTicketNumber;
	}

	public long getAverageWaitingTime() {
		return averageWaitingTime;
	}

	public void setAverageWaitingTime(long averageWaitingTime) {
		this.averageWaitingTime = averageWaitingTime;
	}

	@Override
	public String toString() {
		return "QueueStats [highestGivenTicketNumber=" + highestGivenTicketNumber
				+ ", averageWaitingTime=" + averageWaitingTime + "]";
	}
}

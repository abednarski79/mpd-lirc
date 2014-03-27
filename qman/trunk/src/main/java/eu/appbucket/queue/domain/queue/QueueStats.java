package eu.appbucket.queue.domain.queue;

/**
 * Dynamically calculated information about queue.
 */
public class QueueStats {

	private int highestGivenTicketNumber;
	private int averageWaitingTimeInSeconds;

	public int getHighestGivenTicketNumber() {
		return highestGivenTicketNumber;
	}

	public void setHighestGivenTicketNumber(int highestGivenTicketNumber) {
		this.highestGivenTicketNumber = highestGivenTicketNumber;
	}

	public int getAverageWaitingTimeInSeconds() {
		return averageWaitingTimeInSeconds;
	}

	public void setAverageWaitingTimeInSeconds(int averageWaitingTimeInSeconds) {
		this.averageWaitingTimeInSeconds = averageWaitingTimeInSeconds;
	}

	@Override
	public String toString() {
		return "QueueStats [highestGivenTicketNumber=" + highestGivenTicketNumber
				+ ", averageWaitingTimeInSeconds=" + averageWaitingTimeInSeconds + "]";
	}
}

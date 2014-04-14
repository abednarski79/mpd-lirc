package eu.appbucket.queue.core.domain.queue;

/**
 * Dynamically calculated information about queue.
 */
public class QueueStats {

	private int highestGivenTicketNumber;
	private long averageWaitingTime;
	private QueueInfo queueInfo;
	
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

	public QueueInfo getQueueInfo() {
		return queueInfo;
	}

	public void setQueueInfo(QueueInfo queueInfo) {
		this.queueInfo = queueInfo;
	}
}

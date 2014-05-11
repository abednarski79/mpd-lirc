package eu.appbucket.queue.core.domain.queue;

import java.util.Date;

/**
 * Dynamically calculated information about queue.
 */
public class QueueStats {

	private Integer calculatedAverageWaitingDuration;	
	private QueueInfo queueInfo;
	private Date date;
	
	public Date getDate() {
		return date;
	}

	public void setDate(Date date) {
		this.date = date;
	}

	public Integer getCalculatedAverageWaitingDuration() {
		return calculatedAverageWaitingDuration;
	}

	public void setCalculatedAverageWaitingDuration(
			Integer calculatedAverageWaitingDuration) {
		this.calculatedAverageWaitingDuration = calculatedAverageWaitingDuration;
	}

	public QueueInfo getQueueInfo() {
		return queueInfo;
	}

	public void setQueueInfo(QueueInfo queueInfo) {
		this.queueInfo = queueInfo;
	}
}

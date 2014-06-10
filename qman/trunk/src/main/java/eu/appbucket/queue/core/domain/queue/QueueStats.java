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

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result
				+ ((queueInfo == null) ? 0 : queueInfo.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		QueueStats other = (QueueStats) obj;
		if (queueInfo == null) {
			if (other.queueInfo != null)
				return false;
		} else if (!queueInfo.equals(other.queueInfo))
			return false;
		return true;
	}
}

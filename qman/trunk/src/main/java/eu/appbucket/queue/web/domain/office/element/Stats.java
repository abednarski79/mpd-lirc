package eu.appbucket.queue.web.domain.office.element;

import eu.appbucket.queue.core.domain.queue.QueueStats;

public class Stats {
	private long averageWaitingTime;

	public long getAverageWaitingTime() {
		return averageWaitingTime;
	}

	public void setAverageWaitingTime(long averageWaitingTime) {
		this.averageWaitingTime = averageWaitingTime;
	}
	
	public static Stats fromQueueStats(QueueStats queueStats) {
		Stats stats = new Stats();
		stats.setAverageWaitingTime(queueStats.getAverageWaitingTime());
		return stats;
	}
}

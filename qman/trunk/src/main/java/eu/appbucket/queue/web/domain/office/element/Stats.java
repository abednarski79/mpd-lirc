package eu.appbucket.queue.web.domain.office.element;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;

public class Stats {
	private Integer calculatedAverageWaitingTime;	
	private Integer defaultAverageWaitingTime;
	
	public Integer getCalculatedAverageWaitingTime() {
		return calculatedAverageWaitingTime;
	}

	public void setCalculatedAverageWaitingTime(Integer calcualtedAverageWaitingTime) {
		this.calculatedAverageWaitingTime = calcualtedAverageWaitingTime;
	}
	
	public Integer getDefaultAverageWaitingTime() {
		return defaultAverageWaitingTime;
	}

	public void setDefaultAverageWaitingTime(Integer defaultAverageWaitingTime) {
		this.defaultAverageWaitingTime = defaultAverageWaitingTime;
	}

	public static Stats fromQueueDetailsAndStats(QueueDetails queueDetails, QueueStats queueStats) {
		Stats stats = new Stats();
		stats.setCalculatedAverageWaitingTime(queueStats.getCalculatedAverageWaitingDuration());		
		stats.setDefaultAverageWaitingTime(queueDetails.getDefaultAverageWaitingDuration());
		return stats;
	}
}

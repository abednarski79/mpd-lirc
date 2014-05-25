package eu.appbucket.queue.core.persistence;

import java.util.Collection;
import java.util.Date;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.queue.QueueStats;

public interface QueueDao {
	
	// queuesCache
	public Collection<QueueInfo> getQeueues();
	
	// queueInfoCache
	public QueueInfo getQueueInfoById(int queueId);
	
	// queueDetailsCache
	public QueueDetails getQueueDetailsById(int queueId);
	
	// queueStatsCache
	public QueueStats getQueueStatsByIdAndDate(int queueId, Date statsDate);
	
	// clean: queueStatsCache 
	public void storeQueueStats(QueueStats queueStats);
}

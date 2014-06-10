package eu.appbucket.queue.core.persistence;

import java.util.Collection;
import java.util.Date;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.queue.QueueStats;

public interface QueueDao {
	
	public Collection<QueueInfo> getQeueues();
	
	public QueueInfo getQueueInfoById(int queueId);
	
	public QueueDetails getQueueDetailsById(int queueId);
	
	public QueueStats getQueueStatsByIdAndDate(int queueId, Date statsDate);
	 
	public void storeQueueStats(QueueStats queueStats);
}

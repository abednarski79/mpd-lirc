package eu.appbucket.queue.core.service;

import java.util.Collection;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.queue.QueueStats;

public interface QueueService {
	
	public Collection<QueueInfo> getQeueues();
	public QueueInfo getQueueInfoByQueueId(int queueId);	                 	
	public QueueDetails getQueueDetailsByQueueId(int queueId);
	
	public QueueStats getQueueStatsByQueueId(int queueId);
	public void updateQueueStats(QueueStats queueStats); 
}

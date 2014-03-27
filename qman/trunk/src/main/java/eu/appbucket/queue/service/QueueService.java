package eu.appbucket.queue.service;

import java.util.Collection;

import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueInfo;
import eu.appbucket.queue.domain.queue.QueueStats;

public interface QueueService {
	public Collection<QueueInfo> getQeueues();
	public QueueInfo getQueueInfoByQueueId(int queueId);
	public QueueStats getQueueStatsByQueueId(int queueId);
	public QueueDetails getQueueDetailsByQueueId(int queueId);
}

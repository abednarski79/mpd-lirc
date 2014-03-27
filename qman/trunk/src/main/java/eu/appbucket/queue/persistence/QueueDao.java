package eu.appbucket.queue.persistence;

import java.util.Collection;

import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueInfo;

public interface QueueDao {
	public Collection<QueueInfo> getQeueues();
	public QueueInfo getQueueInfoById(int queueId);
	public QueueDetails getQueueDetailsById(int queueId);
}

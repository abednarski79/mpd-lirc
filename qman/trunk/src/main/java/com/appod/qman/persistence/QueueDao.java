package com.appod.qman.persistence;

import java.util.Collection;

import com.appod.qman.domain.Queue;

public interface QueueDao {
	public Collection<Queue> getQeueues();
	public Queue getQueueById(int queueId);
}

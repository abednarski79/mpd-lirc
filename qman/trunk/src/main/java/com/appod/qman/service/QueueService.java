package com.appod.qman.service;

import java.util.Collection;

import com.appod.qman.domain.Queue;

public interface QueueService {
	public Collection<Queue> getQeueues();
	public Queue getQueueById(int queueId);
}

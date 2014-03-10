package com.appod.qman.service;

import java.util.Collection;
import java.util.HashSet;

import org.springframework.stereotype.Service;

import com.appod.qman.domain.Queue;

@Service
public class QueueServiceMockImpl implements QueueService {
		
	public Collection<Queue> getQeueues() {
		Collection<Queue> colleciton = new HashSet<Queue>();
		colleciton.add(getQueueById(1));
		colleciton.add(getQueueById(2));
		return colleciton;
	}
	
	public Queue getQueueById(int queueId) {
		Queue queue= new Queue();
		queue.setQueueId(queueId);
		queue.setName("Mock queue name " + queueId);
		return queue;
	}
}

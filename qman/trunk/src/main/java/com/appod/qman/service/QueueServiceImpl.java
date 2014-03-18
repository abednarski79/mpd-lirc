package com.appod.qman.service;

import java.util.Collection;
import java.util.HashSet;
import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.appod.qman.domain.Queue;
import com.appod.qman.persistence.QueueDao;

@Service(value="QueueServiceImpl")
public class QueueServiceImpl implements QueueService {
		
	private QueueDao queueDao;
	
	public Collection<Queue> getQeueues() {
		Collection<Queue> colleciton = queueDao.getQeueues();		
		return colleciton;
	}
	
	public Queue getQueueById(int queueId) {
		Queue queue= queueDao.getQueueById(queueId);
		return queue;
	}
	
	@Autowired
	public void setQueueDao(QueueDao queueDao) {
		this.queueDao = queueDao;
	}
}

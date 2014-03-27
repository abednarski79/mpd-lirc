package eu.appbucket.queue.service;

import java.util.Collection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueInfo;
import eu.appbucket.queue.domain.queue.QueueStats;
import eu.appbucket.queue.mock.QueueMockDataGenerater;
import eu.appbucket.queue.persistence.QueueDao;

@Service(value="QueueServiceImpl")
public class QueueServiceImpl implements QueueService {
		
	private QueueDao queueDao;
	
	@Autowired
	public void setQueueDao(QueueDao queueDao) {
		this.queueDao = queueDao;
	}
	
	public Collection<QueueInfo> getQeueues() {
		Collection<QueueInfo> colleciton = queueDao.getQeueues();		
		return colleciton;
	}
	
	public QueueInfo getQueueInfoByQueueId(int queueId) {
		QueueInfo queueInfo= queueDao.getQueueInfoById(queueId);
		return queueInfo;
	}

	public QueueStats getQueueStatsByQueueId(int queueId) {
		return QueueMockDataGenerater.generateMockQueueStats();
	}

	public QueueDetails getQueueDetailsByQueueId(int queueId) {
		QueueDetails queueDetails= queueDao.getQueueDetailsById(queueId);
		return queueDetails;
	}
}

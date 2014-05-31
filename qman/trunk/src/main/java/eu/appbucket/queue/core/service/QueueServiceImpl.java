package eu.appbucket.queue.core.service;

import java.util.Collection;
import java.util.Date;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.persistence.QueueDao;
import eu.appbucket.queue.core.service.util.TimeGenerator;

@Service
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
		Date todayAtMidnight = TimeGenerator.getTodayMidnightDate();
		QueueStats queueStats = queueDao.getQueueStatsByIdAndDate(queueId, todayAtMidnight);
		return queueStats;
	}
	
	public QueueDetails getQueueDetailsByQueueId(int queueId) {
		QueueDetails queueDetails= queueDao.getQueueDetailsById(queueId);
		return queueDetails;
	}
	
	
	public void updateQueueStats(QueueStats queueStats) {
		queueDao.storeQueueStats(queueStats);	
	}
}

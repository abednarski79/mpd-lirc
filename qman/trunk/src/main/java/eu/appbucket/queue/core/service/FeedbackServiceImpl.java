package eu.appbucket.queue.core.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import eu.appbucket.queue.core.domain.feedback.FeedbackRecord;
import eu.appbucket.queue.core.persistence.FeedbackDao;

@Service
public class FeedbackServiceImpl implements FeedbackService {

	private FeedbackDao feedbackDao;
	
	@Autowired
	public void setFeedbackDao(FeedbackDao feedbackDao) {
		this.feedbackDao = feedbackDao;
	}
	
	public void storeTicketEstimation(FeedbackRecord feedbackRecord) {
		feedbackDao.persistFeedbackRecord(feedbackRecord);
	}
	
}

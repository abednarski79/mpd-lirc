package eu.appbucket.queue.core.service;

import eu.appbucket.queue.core.domain.feedback.FeedbackRecord;

public interface FeedbackService {
	
	void storeTicketEstimation(FeedbackRecord feedbackRecord);
}

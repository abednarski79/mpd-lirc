package eu.appbucket.queue.core.persistence;

import eu.appbucket.queue.core.domain.feedback.FeedbackRecord;

public interface FeedbackDao {
	void persistFeedbackRecord(FeedbackRecord record);
}

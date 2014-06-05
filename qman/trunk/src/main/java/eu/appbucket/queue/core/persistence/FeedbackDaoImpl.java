package eu.appbucket.queue.core.persistence;

import eu.appbucket.queue.core.domain.feedback.FeedbackRecord;

public class FeedbackDaoImpl implements FeedbackDao {

	private final static String SQL_INSERT_FEEDBACK_RECORD = 
			"INSERT INTO updates(`queue_id`, `user_ticket`, `served_ticket`, `created`, `quality`) "
			+ "VALUES (?, ?, ?, ?, ?)";
	
	public void persistFeedbackRecord(FeedbackRecord record) {
		
	}

}

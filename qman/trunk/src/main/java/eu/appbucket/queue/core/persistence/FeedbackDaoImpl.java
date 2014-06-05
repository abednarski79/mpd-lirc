package eu.appbucket.queue.core.persistence;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.simple.SimpleJdbcTemplate;
import org.springframework.stereotype.Repository;

import eu.appbucket.queue.core.domain.feedback.FeedbackRecord;

@Repository
public class FeedbackDaoImpl implements FeedbackDao {

	private final static String SQL_INSERT_FEEDBACK_RECORD = 
			"INSERT INTO feedbacks(`rating`, `created`, `comment`, `queue_id`) "
			+ "VALUES (?, ?, ?, ?)";
	
	private SimpleJdbcTemplate jdbcTempalte;
	
	@Autowired
	public void setJdbcTempalte(SimpleJdbcTemplate jdbcTempalte) {
		this.jdbcTempalte = jdbcTempalte;
	}
	
	public void persistFeedbackRecord(FeedbackRecord record) {
		jdbcTempalte.update(SQL_INSERT_FEEDBACK_RECORD, 
				record.getRating().getRatingValue(),
				record.getCreated(),
				record.getComment(),
				record.getQueueInfo() != null ? record.getQueueInfo().getQueueId() : null);
	}
}

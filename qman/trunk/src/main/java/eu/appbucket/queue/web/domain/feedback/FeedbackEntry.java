package eu.appbucket.queue.web.domain.feedback;

import eu.appbucket.queue.web.domain.queue.QueueId;

public class FeedbackEntry {
	
	private QueueId queueId;
	private String comment;
	private int rating;
	
	public QueueId getQueueId() {
		return queueId;
	}
	public void setQueueId(QueueId queueId) {
		this.queueId = queueId;
	}
	public String getComment() {
		return comment;
	}
	public void setComment(String comment) {
		this.comment = comment;
	}
	public int getRating() {
		return rating;
	}
	public void setRating(int rating) {
		this.rating = rating;
	}
}

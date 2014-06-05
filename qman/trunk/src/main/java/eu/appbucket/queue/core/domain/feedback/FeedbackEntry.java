package eu.appbucket.queue.core.domain.feedback;

import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.web.domain.feedback.FeedbackInput;

public class FeedbackEntry {

	private QueueInfo queueInfo;
	private Rating rating;
	private String comment;
	
	public enum Rating {
		
		VERY_BAD(1), POOR(2), FAIR(3), GOOD(4), VERY_GOOD(5);
		
		private int ratingValue;
		
		private Rating(int ratingValue) {
			this.ratingValue = ratingValue;
		}
	}

	public QueueInfo getQueueInfo() {
		return queueInfo;
	}

	public void setQueueInfo(QueueInfo queueInfo) {
		this.queueInfo = queueInfo;
	}

	public Rating getRating() {
		return rating;
	}

	public void setRating(Rating rating) {
		this.rating = rating;
	}

	public String getComment() {
		return comment;
	}

	public void setComment(String comment) {
		this.comment = comment;
	};
	
	public static FeedbackEntry fromFeedbackInput(FeedbackInput feedbackInput) {
		Rating rating = new Rating(feedbackInput.getRating());
		
		return null;
	}
}

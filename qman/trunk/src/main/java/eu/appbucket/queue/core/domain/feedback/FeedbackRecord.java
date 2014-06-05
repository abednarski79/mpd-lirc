package eu.appbucket.queue.core.domain.feedback;

import java.util.Date;

import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.web.domain.feedback.FeedbackEntry;

public class FeedbackRecord {

	private QueueInfo queueInfo;
	private Rating rating;
	private String comment;
	private Date created;
	
	public enum Rating {
		
		VERY_BAD(1), POOR(2), FAIR(3), GOOD(4), VERY_GOOD(5);
		
		private int ratingValue;
		
		private Rating(int ratingValue) {
			this.ratingValue = ratingValue;
		}
		
		public int getRatingValue() {
			return this.ratingValue;
		}
		
		public static Rating getRatingEnumByValue(int ratingValue) {
			switch(ratingValue) {
            case  1: return VERY_BAD;
            case  2: return POOR;
            case  3: return FAIR;
            case  4: return GOOD;
            case  5: return VERY_GOOD;
        }
			return null;
		}
	}

	public Date getCreated() {
		return created;
	}

	public void setCreated(Date created) {
		this.created = created;
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
	
	public static FeedbackRecord fromFeedbackEntryAndQueueInfo(FeedbackEntry feedbackEntry, QueueInfo queueInfo) {
		FeedbackRecord feedbackRecord = new FeedbackRecord();
		Rating rating = Rating.getRatingEnumByValue(feedbackEntry.getRating());
		feedbackRecord.setRating(rating);
		feedbackRecord.setComment(feedbackEntry.getComment());
		feedbackRecord.setQueueInfo(queueInfo);
		feedbackRecord.setCreated(new Date());
		return feedbackRecord;
	}
}

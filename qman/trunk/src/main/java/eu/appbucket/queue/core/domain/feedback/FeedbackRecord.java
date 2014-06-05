package eu.appbucket.queue.core.domain.feedback;

import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.web.domain.feedback.FeedbackEntry;
import eu.appbucket.queue.web.domain.queue.QueueId;

public class FeedbackRecord {

	private QueueInfo queueInfo;
	private Rating rating;
	private String comment;
	
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
	
	public static FeedbackRecord fromFeedbackEntry(FeedbackEntry feedbackEntry) {
		FeedbackRecord feedbackRecord = new FeedbackRecord();
		Rating rating = Rating.getRatingEnumByValue(feedbackEntry.getRating());
		feedbackRecord.setRating(rating);
		feedbackRecord.setComment(feedbackEntry.getComment());
		QueueInfo queueInfo = new QueueInfo();
		QueueId queueIdentificator = feedbackEntry.getQueueId();
		if(queueIdentificator != null) {
			queueInfo.setQueueId(queueIdentificator.getQueueId());
			queueInfo.setName(queueIdentificator.getName());
		}
		feedbackRecord.setQueueInfo(queueInfo);
		return feedbackRecord;
	}
}

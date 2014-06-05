package eu.appbucket.queue.web.controller;

import org.apache.commons.lang3.StringUtils;
import org.apache.log4j.Logger;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.queue.core.domain.feedback.FeedbackRecord;
import eu.appbucket.queue.web.domain.feedback.FeedbackEntry;

public class FeedbackController {
	
	private static final Logger LOGGER = Logger.getLogger(FeedbackController.class);
	
	@RequestMapping(value = "feedbacks", method = RequestMethod.POST)
	@ResponseBody
	public void postFeedback(@RequestBody FeedbackEntry feedbackEntry) {
		Integer queueId = getQueueIdFromFeedback(feedbackEntry);
		LOGGER.info("postFeedback - queueId: " + formatQueueId(queueId) + 
				", rating: " + feedbackEntry.getRating() + 
				", comment: " + formatComment(feedbackEntry.getComment()));
		FeedbackRecord feedbackRecord = FeedbackRecord.fromFeedbackEntry(feedbackEntry);
		
		LOGGER.info("postFeedback.");
	}
	
	private Integer getQueueIdFromFeedback(FeedbackEntry entry) {
		if(entry.getQueueId() == null) {
			return null;
		}
		return entry.getQueueId().getQueueId();
	}
	
	private String formatQueueId(Integer queueId) {
		if(queueId == null) {
			return "NULL";
		}
		return queueId.toString();
	}
	
	private String formatComment(String comment) {
		if(StringUtils.isEmpty(comment)) {
			return "NULL";
		}
		return comment;
	}
}

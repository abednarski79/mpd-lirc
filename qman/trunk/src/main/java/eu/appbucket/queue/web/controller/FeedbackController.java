package eu.appbucket.queue.web.controller;

import org.apache.commons.lang3.StringUtils;
import org.apache.log4j.Logger;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.queue.web.domain.feedback.FeedbackInput;

public class FeedbackController {
	
	private static final Logger LOGGER = Logger.getLogger(FeedbackController.class);
	
	@RequestMapping(value = "feedbacks", method = RequestMethod.POST)
	@ResponseBody
	public void postFeedback(@RequestBody FeedbackInput feedbackInput) {
		Integer queueId = getQueueIdFromFeedback(feedbackInput);
		LOGGER.info("postFeedback - queueId: " + formatQueueId(queueId) + 
				", rating: " + feedbackInput.getRating() + 
				", comment: " + formatComment(feedbackInput.getComment()));
		
		LOGGER.info("postFeedback.");
	}
	
	private Integer getQueueIdFromFeedback(FeedbackInput entry) {
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

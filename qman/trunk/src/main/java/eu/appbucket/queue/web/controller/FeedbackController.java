package eu.appbucket.queue.web.controller;

import org.apache.commons.lang3.StringUtils;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.queue.core.domain.feedback.FeedbackRecord;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.service.FeedbackService;
import eu.appbucket.queue.core.service.QueueService;
import eu.appbucket.queue.web.domain.feedback.FeedbackEntry;

@Controller
public class FeedbackController {
	
	private static final Logger LOGGER = Logger.getLogger(FeedbackController.class);
	private FeedbackService feedbackService;
	private QueueService queueService;
	
	@Autowired
	public void setQueueService(QueueService queueService) {
		this.queueService = queueService;
	}
	
	@Autowired
	public void setFeedbackService(FeedbackService feedbackService) {
		this.feedbackService = feedbackService;
	}
	
	@RequestMapping(value = "feedbacks", method = RequestMethod.POST)
	@ResponseBody
	public void postFeedback(@RequestBody FeedbackEntry feedbackEntry) {
		QueueInfo queueInfo = getQueueInfoFromFeedback(feedbackEntry);
		LOGGER.info("postFeedback - queueInfo: " + queueInfo + 
				", rating: " + feedbackEntry.getRating() + 
				", comment: " + formatComment(feedbackEntry.getComment()));
		FeedbackRecord feedbackRecord = FeedbackRecord.fromFeedbackEntryAndQueueInfo(feedbackEntry, queueInfo);
		feedbackService.storeTicketEstimation(feedbackRecord);
		LOGGER.info("postFeedback.");
	}
	
	private QueueInfo getQueueInfoFromFeedback(FeedbackEntry entry) {
		QueueInfo queueInfo = new QueueInfo();
		Integer queueId = entry.getQueueId();
		if(queueId == null) {
			return queueInfo;
		}
		queueInfo = queueService.getQueueInfoByQueueId(queueId);
		return queueInfo;
	}
	
	private String formatComment(String comment) {
		if(StringUtils.isEmpty(comment)) {
			return "NULL";
		}
		return comment;
	}
}

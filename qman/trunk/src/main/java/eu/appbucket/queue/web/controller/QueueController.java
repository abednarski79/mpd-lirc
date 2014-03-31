package eu.appbucket.queue.web.controller;

import java.util.Collection;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueInfo;
import eu.appbucket.queue.domain.queue.QueueStats;
import eu.appbucket.queue.service.QueueService;

@Controller
public class QueueController {
	
	private static final Logger LOGGER = Logger.getLogger(QueueController.class);
	private QueueService queueService;
	
	@Autowired
	public void setQueueService(QueueService queueService) {
		this.queueService = queueService;
	}
	
	@RequestMapping(value = "queues", method = RequestMethod.GET)
	@ResponseBody
	public Collection<QueueInfo> getListOfQueues() {		
		Collection<QueueInfo> queues = queueService.getQeueues();
		LOGGER.info("queues: " + queues);
		return queues;
	}
	
	@RequestMapping(value = "queues/{queueId}", method = RequestMethod.GET)
	@ResponseBody
	public QueueInfo getQueueInfo(@PathVariable int queueId) {
		LOGGER.info("queueId: " + queueId);
		QueueInfo queueInfo =  queueService.getQueueInfoByQueueId(queueId);
		LOGGER.info("queueInfo: " + queueInfo);
		return queueInfo;
	}
	
	@RequestMapping(value = "queues/{queueId}/queueDetails", method = RequestMethod.GET)
	@ResponseBody
	public QueueDetails getQueueDetails(@PathVariable int queueId) {
		LOGGER.info("queueId: " + queueId);
		QueueDetails queueDetails =  queueService.getQueueDetailsByQueueId(queueId);
		LOGGER.info("queueDetails: " + queueDetails);
		return queueDetails;
	}
	
	@RequestMapping(value = "queues/{queueId}/queueStats", method = RequestMethod.GET)
	@ResponseBody
	public QueueStats getQueueStats(@PathVariable int queueId) {
		LOGGER.info("queueId: " + queueId);
		QueueStats queueStats =  queueService.getQueueStatsByQueueId(queueId);
		LOGGER.info("queueStats: " + queueStats);
		return queueStats;
	}
}

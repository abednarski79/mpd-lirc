package eu.appbucket.queue.web.controller;

import java.util.Collection;
import java.util.HashSet;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.service.QueueService;
import eu.appbucket.queue.web.domain.office.OfficeDetails;
import eu.appbucket.queue.web.domain.queue.QueueId;

@Controller
public class QueueController {
	
	private static final Logger LOGGER = Logger.getLogger(QueueController.class);
	private QueueService queueService;
	
	@Autowired
	public void setQueueService(QueueService queueService) {
		this.queueService = queueService;
	}
	
	@RequestMapping(value = "queues/{queueId}", method = RequestMethod.GET)
	@ResponseBody
	public OfficeDetails getOfficeDetails(@PathVariable int queueId) {
		LOGGER.info("queueId: " + queueId);
		QueueDetails queueDetails =  queueService.getQueueDetailsByQueueId(queueId);
		QueueStats queueStats = queueService.getQueueStatsByQueueId(queueId);
		QueueInfo queueInfo = queueService.getQueueInfoByQueueId(queueId);
		OfficeDetails officeDetails = OfficeDetails.fromQueueData(queueInfo, queueDetails, queueStats);		
		LOGGER.info("officeDetails: " + officeDetails);
		return officeDetails;
	}
	
	@RequestMapping(value = "queues", method = RequestMethod.GET)
	@ResponseBody
	public Collection<QueueId> getListOfQueueIds() {
		Collection<QueueId> queueIds = new HashSet<QueueId>();
		Collection<QueueInfo> queueInfos = queueService.getQeueues();
		for(QueueInfo queueInfo: queueInfos) {
			queueIds.add(QueueId.fromQueueInfo(queueInfo));
		}		
		LOGGER.info("queueIds: " + queueIds);
		return queueIds;
	}
}

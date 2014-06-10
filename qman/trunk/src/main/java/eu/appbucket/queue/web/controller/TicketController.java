package eu.appbucket.queue.web.controller;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;
import eu.appbucket.queue.core.service.QueueService;
import eu.appbucket.queue.core.service.TicketService;
import eu.appbucket.queue.web.domain.ticket.TicketInput;
import eu.appbucket.queue.web.domain.ticket.TicketStatus;

@Controller
public class TicketController {

	private static final Logger LOGGER = Logger.getLogger(TicketController.class);	
	private QueueService queueService;
	private TicketService ticketService;
	
	@Autowired
	public void setQueueService(QueueService queueService) {
		this.queueService = queueService;
	}
	
	@Autowired
	public void setTicketService(TicketService ticketService) {
		this.ticketService = ticketService;
	}
	
	@RequestMapping(value = "queues/{queueId}/tickets/{ticketId}", method = RequestMethod.GET)
	@ResponseBody
	public TicketStatus getTicketStats(@PathVariable int queueId, @PathVariable int ticketId) {		
		LOGGER.info("getTicketStats - queueId: " + queueId + ", ticketId: " + ticketId);
		QueueDetails queueDetails =  queueService.getQueueDetailsByQueueId(queueId);
		QueueStats queueStats = queueService.getQueueStatsByQueueId(queueId);
		TicketEstimation ticketEstimation = ticketService.getTicketEstimation(queueDetails, queueStats, ticketId);
		TicketStatus ticketStatus = TicketStatus.fromTicketEstimation(ticketEstimation);
		LOGGER.info("getTicketStats - " + ticketStatus);
		return ticketStatus;
	}
	
	@RequestMapping(value = "queues/{queueId}/tickets/{ticketId}", method = RequestMethod.POST)
	@ResponseBody
	public TicketStatus postTicketUpdate(@PathVariable int queueId, @PathVariable int ticketId, 
			@RequestBody TicketInput ticketInput) {
		LOGGER.info("postTicketUpdate - queueId: " + queueId + ", ticketId: " + ticketId + ", ticketInput: " + ticketInput);
		QueueInfo queueInfo = queueService.getQueueInfoByQueueId(queueId);
		TicketUpdate ticketUpdate = TicketUpdate.fromTicketInputAndQueueInfo(ticketId, ticketInput, queueInfo);		
		ticketService.processTicketInformation(ticketUpdate);
		QueueDetails queueDetails =  queueService.getQueueDetailsByQueueId(queueId);
		QueueStats queueStats = queueService.getQueueStatsByQueueId(queueId); 
		TicketEstimation ticketEstimation = ticketService.getTicketEstimation(queueDetails, queueStats, ticketId);
		TicketStatus ticketStatus = TicketStatus.fromTicketEstimation(ticketEstimation);
		LOGGER.info("postTicketUpdate - " + ticketStatus);
		return ticketStatus;
	}
}

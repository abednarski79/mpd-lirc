package eu.appbucket.queue.web.controller;

import java.util.Date;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueStats;
import eu.appbucket.queue.domain.ticket.TicketStats;
import eu.appbucket.queue.domain.ticket.TicketUpdate;
import eu.appbucket.queue.service.QueueService;
import eu.appbucket.queue.service.TicketService;

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
	public TicketStats getTicketStats(@PathVariable int queueId, @PathVariable int ticketId) {		
		LOGGER.info("getTicketStats - queueId: " + queueId + ", ticketId: " + ticketId);
		QueueDetails queueDetails =  queueService.getQueueDetailsByQueueId(queueId);
		QueueStats queueStats = queueService.getQueueStatsByQueueId(queueId); 
		TicketStats ticketStats = ticketService.getTicketStatistics(queueDetails, queueStats, ticketId);
		LOGGER.info("getTicketStats - " + ticketStats);
		return ticketStats;
	}
		
	@RequestMapping(value = "queues/{queueId}/tickets/{ticketId}", method = RequestMethod.POST)
	@ResponseBody
	public TicketStats postTicketUpdate(@PathVariable int queueId, @PathVariable int ticketId, 
			@RequestBody TicketUpdate ticketUpdate) {
		LOGGER.info("postTicketUpdate - queueId: " + queueId + ", ticketId: " + ticketId + ", ticketUpdate: " + ticketUpdate);
		ticketService.updateTicketInformation(ticketUpdate);
		QueueDetails queueDetails =  queueService.getQueueDetailsByQueueId(queueId);
		QueueStats queueStats = queueService.getQueueStatsByQueueId(queueId); 
		TicketStats ticketStatus = ticketService.getTicketStatistics(queueDetails, queueStats, ticketId);
		LOGGER.info("postTicketUpdate - " + ticketStatus);
		return ticketStatus;
	}
}

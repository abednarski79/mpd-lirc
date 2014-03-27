package eu.appbucket.queue.controller;

import java.util.Date;

import org.apache.log4j.Logger;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.queue.domain.ticket.TicketStatus;
import eu.appbucket.queue.domain.ticket.TicketUpdate;

@Controller
public class TicketController {

	private static final Logger LOGGER = Logger.getLogger(TicketController.class);
	
	@RequestMapping(value = "queues/{queueId}/tickets/{ticketId}", method = RequestMethod.GET)
	@ResponseBody
	public TicketStatus getTicketStatus(@PathVariable int queueId, @PathVariable int ticketId) {		
		LOGGER.info("getTicketStatus - queueId: " + queueId + ", ticketId: " + ticketId);
		TicketStatus ticketStatus = new TicketStatus();		
		ticketStatus.setWaitingTimeInSeconds(2001);
		LOGGER.info("getTicketStatus - " + ticketStatus);
		return ticketStatus;
	}
		
	@RequestMapping(value = "queues/{queueId}/tickets/{ticketId}", method = RequestMethod.POST)
	@ResponseBody
	public TicketStatus postTicketUpdate(@PathVariable int queueId, @PathVariable int ticketId, 
			@RequestBody TicketUpdate ticketUpdate) {
		LOGGER.info("postTicketUpdate - queueId: " + queueId + ", ticketId: " + ticketId + ", ticketUpdate: " + ticketUpdate);		
		TicketStatus ticketStatus = new TicketStatus();		
		ticketStatus.setWaitingTimeInSeconds(1001);
		LOGGER.info("postTicketUpdate - " + ticketStatus);
		return ticketStatus;
	}
}

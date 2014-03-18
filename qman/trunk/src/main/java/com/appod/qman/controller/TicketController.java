package com.appod.qman.controller;

import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.appod.qman.domain.TicketStatus;
import com.appod.qman.domain.TicketUpdate;

@Controller
@RequestMapping("api")
public class TicketController {

	@RequestMapping(value = "queues/{queueId}/tickets/{ticketId}", method = RequestMethod.GET)
	@ResponseBody
	public TicketStatus getTicketStatus(@PathVariable int queueId, @PathVariable int ticketId) {
		System.out.println("queueId: " + queueId);
		System.out.println("ticketId: " + ticketId);
		TicketStatus ticketStatus = new TicketStatus();		
		ticketStatus.setWaitingTime(new Date().getTime());
		return ticketStatus;
	}
		
	@RequestMapping(value = "queues/{queueId}/tickets/{ticketId}", method = RequestMethod.POST)
	@ResponseBody
	public TicketStatus postTicketUpdate(@PathVariable int queueId, @PathVariable int ticketId, 
			@RequestBody TicketUpdate ticketUpdate) {
		System.out.println("queueTicketNumber: " + ticketUpdate.getQueueTicketNumber());
		return this.getTicketStatus(queueId, ticketId);
	}
}

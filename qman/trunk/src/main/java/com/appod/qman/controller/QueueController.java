package com.appod.qman.controller;

import java.util.Collection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.appod.qman.domain.Queue;
import com.appod.qman.service.QueueService;

@Controller
@RequestMapping("api")
public class QueueController {
	
	private QueueService queueService;
	
	@Autowired
	@Qualifier("QueueServiceImpl")
	public void setQueueService(QueueService queueService) {
		this.queueService = queueService;
	}
	
	@RequestMapping(value = "queues", method = RequestMethod.GET)
	@ResponseBody
	public Collection<Queue> getListOfQueues() {
		return queueService.getQeueues();
	}
	
	@RequestMapping(value = "queues/{queueId}", method = RequestMethod.GET)
	@ResponseBody
	public Queue getQueueStatus(@PathVariable int queueId) {	
		return queueService.getQueueById(queueId);
	}
}

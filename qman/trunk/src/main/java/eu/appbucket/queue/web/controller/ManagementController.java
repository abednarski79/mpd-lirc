package eu.appbucket.queue.web.controller;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.queue.core.service.ManagementService;

@Controller
public class ManagementController {
	
	private static final Logger LOGGER = Logger.getLogger(ManagementController.class);
	private ManagementService managementService;
	
	@Autowired
	public void setManagementService(ManagementService managementService) {
		this.managementService = managementService;
	}
	
	@RequestMapping(value = "resetCache", method = RequestMethod.GET)
	@ResponseBody
	public void resetCache() {
		LOGGER.info("resetCache");
		managementService.resetCache();
		LOGGER.info("resetCache.");
	}
}

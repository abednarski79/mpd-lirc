package eu.appbucket.bicycle.web.controller;

import java.util.Date;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.bicycle.core.domain.report.ReportData;
import eu.appbucket.bicycle.core.service.ReportService;
import eu.appbucket.bicycle.web.domain.report.ReportEntry;

@Controller
public class ReportController {

	private static final Logger LOGGER = Logger.getLogger(ReportController.class);	
	private ReportService reportService;
	
	@Autowired
	public void setReportService(ReportService reportService) {
		this.reportService = reportService;
	}
	
	@RequestMapping(value = "reports", method = RequestMethod.POST)
	@ResponseBody
	public void postReportEntry(@RequestBody ReportEntry reportEntry) {
		LOGGER.info("postReportEntry");
		ReportData reportData = ReportData.fromReportEntry(reportEntry);
		reportData.setCreated(new Date());
		reportService.saveReportData(reportData);
		LOGGER.info("postReportEntry");
	}
}

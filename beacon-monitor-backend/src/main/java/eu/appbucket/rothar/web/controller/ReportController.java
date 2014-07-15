package eu.appbucket.rothar.web.controller;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.appbucket.rothar.core.domain.report.ReportData;
import eu.appbucket.rothar.core.service.ReportService;
import eu.appbucket.rothar.web.domain.report.ReportEntry;

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
	
	@RequestMapping(value = "reports", method = RequestMethod.GET)
	@ResponseBody
	public List<ReportEntry> getReportEntries() {
		LOGGER.info("getReportEntries");
		LOGGER.info("getReportEntries");
		ReportEntry entry = null;
		List<ReportEntry> reportsEntries = new ArrayList<ReportEntry>(); 
		List<ReportData> reportsData = this.reportService.getReportsData();
		for(ReportData reportData: reportsData) {
			entry = ReportEntry.fromReportData(reportData);
			entry.setUrl("https://maps.google.com/?q="+ entry.getLatitude() +","+entry.getLongitude());
			reportsEntries.add(entry);
		}
		return reportsEntries;
	}
}

package eu.appbucket.bicycle.core.service;

import org.springframework.stereotype.Service;

import eu.appbucket.bicycle.core.domain.report.ReportData;
import eu.appbucket.bicycle.core.persistence.ReportDao;

@Service
public class ReportServiceImpl implements ReportService {

	private ReportDao reportDao;
	
	public void setReportDao(ReportDao reportDao) {
		this.reportDao = reportDao;
	}
	
	public void saveReportData(ReportData reportData) {
		reportDao.createNewEntry(reportData);
	}

}

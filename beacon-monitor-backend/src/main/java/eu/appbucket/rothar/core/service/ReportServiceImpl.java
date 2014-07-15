package eu.appbucket.rothar.core.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import eu.appbucket.rothar.core.domain.report.ReportData;
import eu.appbucket.rothar.core.persistence.ReportDao;

@Service
public class ReportServiceImpl implements ReportService {

	private ReportDao reportDao;
	
	@Autowired
	public void setReportDao(ReportDao reportDao) {
		this.reportDao = reportDao;
	}
	
	public void saveReportData(ReportData reportData) {
		reportDao.createNewEntry(reportData);
	}

	public List<ReportData> getReportsData() {
		return reportDao.getAllReportEntries();
	}

}	

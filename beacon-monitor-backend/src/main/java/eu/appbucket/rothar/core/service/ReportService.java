package eu.appbucket.rothar.core.service;

import java.util.List;

import eu.appbucket.rothar.core.domain.report.ReportData;

public interface ReportService {
	void saveReportData(ReportData reportData);
	List<ReportData> getReportsData();
}

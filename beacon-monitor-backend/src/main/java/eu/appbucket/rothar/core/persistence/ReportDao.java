package eu.appbucket.rothar.core.persistence;

import java.util.List;

import eu.appbucket.rothar.core.domain.report.ReportData;

public interface ReportDao {
	
	void createNewEntry(ReportData reportData);
	List<ReportData> getAllReportEntries();
}

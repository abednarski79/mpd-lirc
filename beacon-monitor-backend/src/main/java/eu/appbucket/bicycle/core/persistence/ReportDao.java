package eu.appbucket.bicycle.core.persistence;

import eu.appbucket.bicycle.core.domain.report.ReportData;

public interface ReportDao {
	
	void createNewEntry(ReportData reportData);
}
